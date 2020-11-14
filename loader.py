import subprocess as sub, hashlib, random, os


def run():
    sub.call(['qemu-system-i386', 'loader.bin'])


def generate():
    if not os.path.isfile("define.asm"): open('define.asm', 'w')
    if not os.path.isfile("select.asm"):  open('select.asm', 'w')
    if not os.path.isfile("execute.asm"): open('execute.asm', 'w')
    f = open('loader.asm', 'w')
    f.write('''
org 0x7C00   ; add 0x7C00 to label addresses
 bits 16      ; tell the assembler we want 16 bit code

   mov ax, 0  ; set up segments
   mov ds, ax
   mov es, ax
   mov ss, ax     ; setup stack
   mov sp, 0x7C00 ; stack grows downwards from 0x7C00

 tty1:

   mov si, prompt
   call print_string

   mov di, buffer
   call get_string

   mov si, buffer
   cmp byte [si], 0  ; blank line?
   je tty1       ; yes, ignore it

  %include 'define.asm'

   mov si,badcommand
   call print_string 
   jmp tty1  

  %include 'select.asm'

 badcommand db 'Bad command entered.', 0x0D, 0x0A, 0
 prompt db '>', 0
 %include 'execute.asm'
 buffer times 64 db 0


 ; ================
 ; calls start here
 ; ================

 print_string:
   lodsb        ; grab a byte from SI

   or al, al  ; logical or AL by itself
   jz .done   ; if the result is zero, get out

   mov ah, 0x0E
   int 0x10      ; otherwise, print out the character!

   jmp print_string

 .done:
   ret

 get_string:
   xor cl, cl

 .loop:
   mov ah, 0
   int 0x16   ; wait for keypress

   cmp al, 0x08    ; backspace pressed?
   je .backspace   ; yes, handle it

   cmp al, 0x0D  ; enter pressed?
   je .done      ; yes, we're done

   cmp cl, 0x3F  ; 63 chars inputted?
   je .loop      ; yes, only let in backspace and enter

   mov ah, 0x0E
   int 0x10      ; print out character

   stosb  ; put character in buffer
   inc cl
   jmp .loop

 .backspace:
   cmp cl, 0	; beginning of string?
   je .loop	; yes, ignore the key

   dec di
   mov byte [di], 0	; delete character
   dec cl		; decrement counter as well

   mov ah, 0x0E
   mov al, 0x08
   int 10h		; backspace on the screen

   mov al, ' '
   int 10h		; blank character out

   mov al, 0x08
   int 10h		; backspace again

   jmp .loop	; go to the main loop

 .done:
   mov al, 0	; null terminator
   stosb

   mov ah, 0x0E
   mov al, 0x0D
   int 0x10
   mov al, 0x0A
   int 0x10		; newline

   ret

 strcmp:
 .loop:
   mov al, [si]   ; grab a byte from SI
   mov bl, [di]   ; grab a byte from DI
   cmp al, bl     ; are they equal?
   jne .notequal  ; nope, we're done.

   cmp al, 0  ; are both bytes (they were equal before) null?
   je .done   ; yes, we're done.

   inc di     ; increment DI
   inc si     ; increment SI
   jmp .loop  ; loop!

 .notequal:
   clc  ; not equal, clear the carry flag
   ret

 .done: 	
   stc  ; equal, set the carry flag
   ret

   times 510-($-$$) db 0
   dw 0AA55h ; some BIOSes require this signature
    ''')
    f.close()
    sub.call(['nasm', 'loader.asm', '-o', 'loader.bin'])
    os.remove('loader.asm')
    if os.path.isfile("define.asm"): os.remove('define.asm')
    if os.path.isfile("select.asm"): os.remove('select.asm')
    if os.path.isfile("execute.asm"): os.remove('execute.asm')


def print(value):
    randvar = str(random.randint(1, 1000))
    randhash = hashlib.md5(randvar.encode()).hexdigest()
    f = open('select.asm', 'a')
    f.write(f'''
    mov si, kvar_{randhash}
    call print_string

    ''')
    f.close()

    f = open('execute.asm', 'a')
    f.write(f'''
    kvar_{randhash} db '{value}',0x0a,0x0d,0
    ''')


def asm(value):
    f = open('select.asm', 'a')
    f.write(f'''
{value}
    ''')
    f.close()


def end():
    f = open('select.asm', 'a')
    f.write(f'''
  jmp tty1
    ''')
    f.close()


def start(name):
    f = open('define.asm', 'a')
    f.write(f'''
   mov si, buffer
   mov di, cmd_{name}  ; "hi" command
   call strcmp
   jc .{name}
''')
    f.close()

    f = open('select.asm', 'a')
    f.write(f'''
.{name}:
    ''')
    f.close()

    f = open('execute.asm', 'a')
    f.write(f'''
 cmd_{name} db '{name}', 0
     ''')
    f.close()