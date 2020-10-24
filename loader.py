'''
    In the name of God, the Compassionate, the Merciful
    Loader Os (c) 2020 Mani Jamali. All rights reserved
'''

import os,sys,subprocess,random,shutil

filename = 'core/kernel.tmp'

# Enums #

# Color enum #
class color:
    black = 0
    blue = 1
    green = 2
    cyan = 3
    red = 4
    magenta = 5
    brown = 6
    grey = 7
    dark_grey = 8
    light_blue = 9
    light_green = 10
    light_cyan = 11
    light_red = 12
    light_magenta = 13
    yellow = 14
    white = 15

# type enum #
class type:
    char = 0
    string = 1
    short = 2
    int = 3
    long = 4
    float = 5
    double = 6
    ushort = 7
    uint = 8
    ulong = 9

# show types enum #
class show_type:
    ok_start = 0     # [ OK ] Start name process.
    ok_end = 1       # [ OK ] End name process.
    fail_start = 2   # [FAIL] Fail to start name process.
    ok = 3           # name: message
    error = 4        # name: error: message
    warning = 5      # name: warning: message
    power_on = 6
    power_off = 7
    restart = 8


# Kernel driver #
class kernel:
    name = ''
    def __init__(self,name):
        self.name = name

        if not os.path.isdir ('debug'): os.mkdir('debug')
        if os.path.isfile('core/kernel.tmp'): os.remove('core/kernel.tmp')

    # generate the kernel file #
    def generate(self):
        # kernel.c
        main_start = '''
#include "kernel.h"
void __stack_chk_fail(){} void kernel_entry()
{
unsigned long _ki = 0;
char* _kchar = "";
        '''
        main_end = '}'

        file = open ('core/kernel.tmp','r')
        main_body = file.read()
        file.close()

        file = open ('core/kernel.c','w')
        file.write(main_start+main_body+main_end) # Write into kernel
        file.close()

        # Compile boot #
        boot = 'as --32 core/boot.s -o debug/boot.o'
        boot = boot.split(' ')
        subprocess.call(boot)

        # Compile kernel #
        kernel = 'gcc -m32 -c core/kernel.c -o debug/kernel.o -std=gnu99 -ffreestanding -O2 -Wall -Wextra'
        kernel = kernel.split(' ')
        subprocess.call(kernel)

        # Compile utils #
        utils = 'gcc -m32 -c core/utils.c -o debug/utils.o -std=gnu99 -ffreestanding -O2 -Wall -Wextra'
        utils = utils.split(' ')
        subprocess.call(utils)

        # Compile char #
        char = 'gcc -m32 -c core/char.c -o debug/char.o -std=gnu99 -ffreestanding -O2 -Wall -Wextra'
        char = char.split(' ')
        subprocess.call(char)

        # Link the kernel #
        link = 'ld -m elf_i386 -T core/linker.ld debug/kernel.o debug/utils.o debug/char.o debug/boot.o -o debug/kernel.bin -nostdlib'
        link = link.split(' ')
        subprocess.call(link)

        shutil.copyfile('debug/kernel.bin',self.name)
        
    # run the kernel file #
    def run(self):
        # Run the kernel #
        subprocess.call(['qemu-system-i386', '-kernel', self.name])

    # reboot syscall command #
    def reboot (self):
        file = open(filename, 'a')
        file.write('reboot();')
        file.close()

# VGA Driver #
class io:

    fgcolor = 15
    bgcolor = 0

    # Clear screen #
    def clear (self):
        # Write into kernel #
        file = open (filename,'a')
        file.write ('init_vga ('+str(self.fgcolor)+','+str(self.bgcolor)+');')
        file.close()

    # Color #
    def color (self,bg,fg):
        # Write into kernel #
        file = open(filename, 'a')
        file.write('init_vga ('+str(fg)+','+str(bg)+');')
        file.close()

        self.bgcolor = bg
        self.fgcolor = fg

    # Print #
    def print (self,text):
        file = open(filename, 'a')
        file.write('print_string("'+text+'",'+str(self.fgcolor)+','+str(self.bgcolor)+');')
        file.close()

    # print blocks in vfs #
    def print_data (self,block):
        file = open(filename, 'a')
        file.write('print_string(data['+str(block)+'],' + str(self.fgcolor) + ',' + str(self.bgcolor) + ');')
        file.close()

    # print addr in vfs #
    def print_addr (self,block):
        file = open(filename, 'a')
        file.write('print_string(addr['+str(block)+'],' + str(self.fgcolor) + ',' + str(self.bgcolor) + ');')
        file.close()

    # Print with line #
    def println (self,text):
        file = open(filename, 'a')
        file.write('print_string("' + text + '",'+str(self.fgcolor)+','+str(self.bgcolor)+');print_new_line('+str(self.fgcolor)+','+str(self.bgcolor)+');')
        file.close()

    # Print a new line #
    def newline (self):
        file = open(filename, 'a')
        file.write('print_new_line('+str(self.fgcolor)+','+str(self.bgcolor)+');')
        file.close()

    # Print integer #
    def printint (self,num):
        file = open(filename, 'a')
        file.write(
            'print_int(' + str(num) + ',' + str(self.fgcolor) + ',' + str(self.bgcolor) + ');print_new_line(' + str(
                self.fgcolor) + ',' + str(self.bgcolor) + ');')
        file.close()

    # Read int #
    def readint (self,var,message):
        file = open(filename, 'a')
        file.write(
            ('print_string ("'+str(message)+'",'+str(self.fgcolor)+','+str(self.bgcolor)+'); {name} = read_int(' + str(self.fgcolor) + ',' + str(self.bgcolor) + ');')
            .replace('{name}',var.replace("${",'_vfs_kvariable_').replace("}",'_'))
        )

        file.close()

    # Read Char #
    def readchar (self,var,message):
        file = open(filename, 'a')
        file.write(
            ('print_string ("' + str(message) + '",' + str(self.fgcolor) + ',' + str(
                self.bgcolor) + '); {name} = read_char(' + str(self.fgcolor) + ',' + str(self.bgcolor) + ');')
                .replace('{name}', var.replace("${", '_vfs_kvariable_').replace("}", '_'))
        )

        file.close()

    # Read String #
    def read (self,var,message):
        file = open(filename, 'a')
        file.write(
            ('print_string ("' + str(message) + '",' + str(self.fgcolor) + ',' + str(
                self.bgcolor) + '); {name} = read_string(' + str(self.fgcolor) + ',' + str(self.bgcolor) + ');')
                .replace('{name}', var.replace("${", '_vfs_kvariable_').replace("}", '_'))
        )

        file.close()

    def show_message (self,name,type,message):
        file = open(filename, 'a')
        if type==0:
            file.write('''
            print_string ("[ ",{fgcolor},{bgcolor});
            print_string ("OK",BRIGHT_GREEN,{bgcolor});
            print_string (" ] ",{fgcolor},{bgcolor});
            print_string ("Start {name} process.",{fgcolor},{bgcolor});
            print_new_line({fgcolor},{bgcolor});
            '''
                       .replace('{bgcolor}',str(self.bgcolor))
                       .replace('{name}',name)
                       .replace('{fgcolor}', str(self.fgcolor))
            )
        elif type==1:
            file.write('''
            print_string ("[ ",{fgcolor},{bgcolor});
            print_string ("OK",BRIGHT_GREEN,{bgcolor});
            print_string (" ] ",{fgcolor},{bgcolor});
            print_string ("End {name} process.",{fgcolor},{bgcolor});
            print_new_line({fgcolor},{bgcolor});
            '''
                       .replace('{bgcolor}',str(self.bgcolor))
                       .replace('{name}',name)
                       .replace('{fgcolor}', str(self.fgcolor))
            )
        elif type==2:
            file.write('''
            print_string ("[",{fgcolor},{bgcolor});
            print_string ("FAIL",RED,{bgcolor});
            print_string ("] ",{fgcolor},{bgcolor});
            print_string ("Fail to start {name} process.",{fgcolor},{bgcolor});
            print_new_line({fgcolor},{bgcolor});
            '''
                       .replace('{bgcolor}',str(self.bgcolor))
                       .replace('{name}',name)
                       .replace('{fgcolor}',str(self.fgcolor))
            )
        elif type==3:
            file.write('''
            print_string ("{name}: {message}.",BRIGHT_GREEN,{bgcolor});
            print_new_line({fgcolor},{bgcolor});
            '''
                       .replace('{bgcolor}',str(self.bgcolor))
                       .replace('{name}',name)
                       .replace('{message}',message)
                       .replace('{fgcolor}',str(self.fgcolor))
            )
        elif type==4:
            file.write('''
            print_string ("{name}: error: {message}.",RED,{bgcolor});
            print_new_line({fgcolor},{bgcolor});
            '''
                       .replace('{bgcolor}',str(self.bgcolor))
                       .replace('{name}',name)
                       .replace('{message}',message)
                       .replace('{fgcolor}',str(self.fgcolor))
            )
        elif type==5:
            file.write('''
            print_string ("{name}: warning: {message}.",YELLOW,{bgcolor});
            print_new_line({fgcolor},{bgcolor});
            '''
                       .replace('{bgcolor}',str(self.bgcolor))
                       .replace('{name}',name)
                       .replace('{message}',message)
                       .replace('{fgcolor}',str(self.fgcolor))
            )
        elif type==6:
            file.write('''
                        print_string ("[ ",{fgcolor},{bgcolor});
                        print_string ("OK",BRIGHT_GREEN,{bgcolor});
                        print_string (" ] ",{fgcolor},{bgcolor});
                        print_string ("Power on the kernel.",{fgcolor},{bgcolor});
                        print_new_line({fgcolor},{bgcolor});
                        '''
                       .replace('{bgcolor}', str(self.bgcolor))
                       .replace('{fgcolor}', str(self.fgcolor))
                       )
        elif type==7:
            file.write('''
                                    print_string ("[ ",{fgcolor},{bgcolor});
                                    print_string ("OK",BRIGHT_GREEN,{bgcolor});
                                    print_string (" ] ",{fgcolor},{bgcolor});
                                    print_string ("Power off the kernel.",{fgcolor},{bgcolor});
                                    print_new_line({fgcolor},{bgcolor});
                                    '''
                       .replace('{bgcolor}', str(self.bgcolor))
                       .replace('{fgcolor}', str(self.fgcolor))
                       )
        elif type==8:
            file.write('''
                                    print_string ("[ ",{fgcolor},{bgcolor});
                                    print_string ("OK",BRIGHT_GREEN,{bgcolor});
                                    print_string (" ] ",{fgcolor},{bgcolor});
                                    print_string ("Restart the kernel.",{fgcolor},{bgcolor});
                                    print_new_line({fgcolor},{bgcolor});
                                    '''
                       .replace('{bgcolor}', str(self.bgcolor))
                       .replace('{fgcolor}', str(self.fgcolor))
                       )
        file.close()

# VFS #
class vfs:
    def blocks (self,blocknumber):
        i = 0
        file = open(filename, 'a')
        file.write('unsigned long blocks = '+str(blocknumber)+";")
        file.close()
        file = open(filename, 'a')
        file.write('char* addr[] = {')
        file.close()
        while i<=blocknumber-1:
            file = open(filename, 'a')
            file.write('"",')
            file.close()
            i+=1
        file = open(filename, 'a')
        file.write('};')
        file.close()

        i = 0

        file = open(filename, 'a')
        file.write('char* data[] = {')
        file.close()
        while i <= blocknumber - 1:
            file = open(filename, 'a')
            file.write('"",')
            file.close()
            i += 1
        file = open(filename, 'a')
        file.write('};')
        file.close()

    def addblock (self,block,addr,data):
        file = open(filename, 'a')
        file.write('''
        addr[{block}]="{addr}";
        data[{block}]="{data}";
        '''.replace("{addr}",addr).replace("{block}",str(block)).replace("{data}",data))
        file.close()

# Time driver #
class time:

    # Sleep in io #
    def sleep (self,times):
        file = open(filename, 'a')
        file.write('sleep ('+str(times)+');')
        file.close()

class ttychar:
    prompt = '/: '
    addr_prompt = 0
    addr_fgcolor = color.light_blue
    bgcolor = color.black
    fgcolor = color.white
    start_timeout = 2
    end_timeout = 2

    def start (self):
        file = open (filename,'a')
        file.write ('while (1){sleep ({start_timeout});print_string ({addr},{addrfgcolor},{bgcolor});print_string ("{prompt}",{fgcolor},{bgcolor});char _vfs_kvariable_cmd_ = read_char ({fgcolor},{bgcolor});switch (_vfs_kvariable_cmd_){'
                    .replace('{prompt}',self.prompt)
                    .replace('{addr}', "addr["+str(self.addr_prompt)+"]")
                    .replace('{bgcolor}',str(self.bgcolor))
                    .replace('{fgcolor}',str(self.fgcolor))
                    .replace('{addrfgcolor}', str(self.addr_fgcolor))
                    .replace('{start_timeout}',str(self.start_timeout))
        )
        file.close()

    def end (self):
        file = open(filename, 'a')
        file.write('}sleep({0});}'.replace("{0}",str(self.end_timeout)))
        file.close()

    def define (self,char):
        file = open(filename,'a')
        file.write('case \''+char+'\':')
        file.close()

    def enddef (self):
        file = open(filename, 'a')
        file.write('break;')
        file.close()