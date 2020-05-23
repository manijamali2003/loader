# Python Loader Compiler #

import sys, os

python_file = sys.argv[1]

file = open (python_file,'r')
strv = file.read()
file.close()

strv = strv.split("\n")
sstrv = ''

for i in strv:
    ## Comments ##
    if i.startswith ("#"):
        i = ''

    elif i.__contains__("(") and i.__contains__(")") and not i.__contains__('def'):
        # hello ()
        # pyc_hello ()
        # pyc_hello ();
        i = i.replace("'",'"')+";"

    elif i.__contains__("="):
        # i = 0
        i = i.split("=")

        ## Check numberic variable ##
        if not (i[1].__contains__('"') or i[1].__contains__("'")) and not i[1].__contains__("."):
            i = "long " + i[0] + " = " + i[1] + ";"
        elif not (i[1].__contains__('"') or i[1].__contains__("'")) and i[1].__contains__("."):
            i = "double " + i[0] + " = " + i[1] +";"
        else:
            i = "char* "+i[0]+" = \""+i[1].replace("'","").replace('"',"")+"\";"

    sstrv = sstrv + "\n" + i

print (sstrv)

file = open ('kernel.c','w')
file.write ('#include "kernel.h"\n')
file.write ('int kernel_entry() {init_vga(WHITE, BLACK);')
file.write (sstrv)
file.write ('return 0;}')
file.close()

boot_S = """
# set magic number to 0x1BADB002 to identified by bootloader 
.set MAGIC,    0x1BADB002

# set flags to 0
.set FLAGS,    0

# set the checksum
.set CHECKSUM, -(MAGIC + FLAGS)

# set multiboot enabled
.section .multiboot

# define type to long for each data defined as above
.long MAGIC
.long FLAGS
.long CHECKSUM


# set the stack bottom 
stackBottom:

# define the maximum size of stack to 512 bytes
.skip 1024


# set the stack top which grows from higher to lower
stackTop:

.section .text
.global _start
.type _start, @function


_start:

  # assign current stack pointer location to stackTop
	mov $stackTop, %esp

  # call the kernel main source
	call kernel_entry

	cli


# put system in infinite loop
hltLoop:

	hlt
	jmp hltLoop

.size _start, . - _start

"""

linkerd_LD = """
/* entry point of our kernel */
ENTRY(_start)

SECTIONS
{
	/* we need 1MB of space atleast */
	. = 1M;

  	/* text section */
	.text BLOCK(4K) : ALIGN(4K)
	{
		*(.multiboot)
		*(.text)
	}

	/* read only data section */
	.rodata BLOCK(4K) : ALIGN(4K)
	{
		*(.rodata)
	}

	/* data section */
	.data BLOCK(4K) : ALIGN(4K)
	{
		*(.data)
	}

	/* bss section */
	.bss BLOCK(4K) : ALIGN(4K)
	{
		*(COMMON)
		*(.bss)
	}

}

"""

# Create Boot file ##
file = open ("boot.s","w")
file.write(boot_S)
file.close()

# Create Linker file ##
file = open ("linker.ld","w")
file.write(linkerd_LD)
file.close()


## Compile Boot S ##
os.system ("as --32 boot.s -o boot.o")

## Compile kernel.c ##
os.system ("gcc -m32 -c kernel.c -o kernel.o -std=gnu99 -ffreestanding -O2 -Wall -Wextra".replace("kernel.c",python_file.replace(".py",".c")))

## Link the compiled files ##
os.system ("ld -m elf_i386 -T linker.ld kernel.o boot.o -o loader.pyc -nostdlib".replace('kernel.o',python_file.replace(".py",".o")).replace("loader.pyc",python_file.replace(".py",".pyc")))

## Remove Boot and kernel file and ld file ##

os.remove (python_file.replace(".py",".c"))
os.remove ("boot.s")
os.remove ("linker.ld")
os.remove (python_file.replace(".py",".o"))
os.remove ("boot.o")