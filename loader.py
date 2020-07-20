'''
    In the name of God, the Compassionate, the Merciful
    Loader Os (c) 2020 Mani Jamali. All rights reserved
'''

import os,sys,subprocess,random,shutil

## Enums ##
class colors:
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

    # inside/switch #
class sysinfo:
    mode = 'inside'

class show_type:
    ok_start = 0     # [ OK ] Start name process.
    ok_end = 1       # [ OK ] End name process.
    fail_start = 2   # [FAIL] Fail to start name process.
    ok = 3           # name: message
    error = 4        # name: error: message
    warning = 5      # name: warning: message

## Kernel driver ##
class kernel:
    name = ''
    def __init__(self,name):
        self.name = name

        if os.path.isfile('core/kernel.tmp'): os.remove('core/kernel.tmp')
        if os.path.isfile('core/kernel_switchs.h'):
            os.remove('core/kernel_switchs.h')
            open ('core/kernel_switchs.h','w')

    def generate(self):
        ## kernel.c
        main_start = '''
#include "kernel.h"
#include "kernel_switchs.h"
void __stack_chk_fail(){} void kernel_entry()
{
        '''
        main_end = '}'

        file = open ('core/kernel.tmp','r')
        main_body = file.read()
        file.close()

        file = open ('core/kernel.c','w')
        file.write(main_start+main_body+main_end) ## Write into kernel
        file.close()

        ## Compile boot ##
        boot = 'as --32 core/boot.s -o debug/boot.o'
        boot = boot.split(' ')
        subprocess.call(boot)

        ## Compile kernel ##
        kernel = 'gcc -m32 -c core/kernel.c -o debug/kernel.o -std=gnu99 -ffreestanding -O2 -Wall -Wextra'
        kernel = kernel.split(' ')
        subprocess.call(kernel)

        ## Compile utils ##
        utils = 'gcc -m32 -c core/utils.c -o debug/utils.o -std=gnu99 -ffreestanding -O2 -Wall -Wextra'
        utils = utils.split(' ')
        subprocess.call(utils)

        ## Compile char ##
        char = 'gcc -m32 -c core/char.c -o debug/char.o -std=gnu99 -ffreestanding -O2 -Wall -Wextra'
        char = char.split(' ')
        subprocess.call(char)

        ## Link the kernel ##
        link = 'ld -m elf_i386 -T core/linker.ld debug/kernel.o debug/utils.o debug/char.o debug/boot.o -o debug/kernel.bin -nostdlib'
        link = link.split(' ')
        subprocess.call(link)

        shutil.copyfile('debug/kernel.bin',self.name)
    def run(self):
        ## Run the kernel ##
        subprocess.call(['qemu-system-i386', '-kernel', self.name])

    def define (self,type,name,value):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        file = open(filename, 'a')
        file.write(type+' _switch_variable_'+name+"_ = "+value+";")
        file.close()

## VGA Driver ##
class vga:

    fgcolor = 15
    bgcolor = 0

    ## Clear screen ##
    def clear (self):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        ## Write into kernel ##
        file = open (filename,'a')
        file.write ('init_vga ('+str(self.fgcolor)+','+str(self.bgcolor)+');')
        file.close()

    ## Color ##
    def color (self,bg,fg):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        ## Write into kernel ##
        file = open(filename, 'a')
        file.write('init_vga ('+str(fg)+','+str(bg)+');')
        file.close()

        self.bgcolor = bg
        self.fgcolor = fg

    ## Print ##
    def print (self,text):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        if text.startswith("$"):
            file = open(filename, 'a')
            file.write('print_string(_switch_variable_' + text.replace('$','')+ '_,' + str(self.fgcolor) + ',' + str(self.bgcolor) + ');')
            file.close()
        else:
            file = open(filename, 'a')
            file.write('print_string("'+text+'",'+str(self.fgcolor)+','+str(self.bgcolor)+');')
            file.close()

    ## Print with line ##
    def println (self,text):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        if text.startswith ('$'):
            file = open(filename, 'a')
            file.write('print_string(_switch_variable_' + text.replace('$','') + '_,' + str(self.fgcolor) + ',' + str(
                self.bgcolor) + ');print_new_line(' + str(self.fgcolor) + ',' + str(self.bgcolor) + ');')
            file.close()
        else:
            file = open(filename, 'a')
            file.write('print_string("' + text + '",'+str(self.fgcolor)+','+str(self.bgcolor)+');print_new_line('+str(self.fgcolor)+','+str(self.bgcolor)+');')
            file.close()

    ## Print a new line ##
    def newline (self):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        file = open(filename, 'a')
        file.write('print_new_line('+str(self.fgcolor)+','+str(self.bgcolor)+');')
        file.close()

    ## Print integer ##
    def printint (self,num):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        file = open(filename, 'a')
        file.write(
            'print_int(' + str(num) + ',' + str(self.fgcolor) + ',' + str(self.bgcolor) + ');print_new_line(' + str(
                self.fgcolor) + ',' + str(self.bgcolor) + ');')
        file.close()

    ## Show integer variable ##
    def showint (self,var):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        file = open(filename, 'a')
        file.write(
            'print_int(_switch_variable_' + str(var).replace('$','') + '_,' + str(self.fgcolor) + ',' + str(self.bgcolor) + ');print_new_line(' + str(
                self.fgcolor) + ',' + str(self.bgcolor) + ');')
        file.close()

    ## Input int ##
    def inputint (self,var,message):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        file = open(filename, 'a')
        file.write(
            'print_string ("'+str(message)+'",'+str(self.fgcolor)+','+str(self.bgcolor)+'); _switch_variable_'+
            var.replace('$','')+'_ = read_int(' + str(self.fgcolor) + ',' + str(self.bgcolor) + ');'
        )

        file.close()

    def show_message (self,name,type,message):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
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
        file.close()

## Time driver ##
class time:

    ## Sleep in io ##
    def sleep (self,times):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        file = open(filename, 'a')
        file.write('sleep ('+str(times)+');')
        file.close()

    ## Start loop ##
    def startloop (self,start,end):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        ra = random.randint (1,1000000)
        self.ra = ra
        file = open(filename, 'a')
        file.write('unsigned long _loop_variable_{0} = {1};while (_loop_variable_{0} <= {2}){'.replace('{0}',str(ra)).replace('{1}',str(start)).replace('{2}',str(end)))
        file.close()

    ## End loop ##
    def endloop (self):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        file = open(filename, 'a')
        file.write('}')
        file.close()

    ## Counter for loop ##
    def counter (self,number):
        if sysinfo.mode == 'inside':
            filename = 'core/kernel.tmp'
        else:
            filename = 'core/kernel_switchs.h'
        file = open(filename, 'a')
        file.write('_loop_variable_'+str(self.ra)+" = _loop_variable_"+str(self.ra)+' + '+str(number)+";")
        file.close()

class switch:
    def startswitch (self,var):
        file = open('core/kernel.tmp', 'a')
        file.write('''
        switch ({var}){
        '''.replace('{var}',"_switch_variable_"+var.replace("$","")+"_"))
        file.close()

    def start(self,name):
        file = open('core/kernel_switchs.h', 'a')
        file.write('void _switch_function_'+name+"_ (char* args){")
        file.close()

        sysinfo.mode = 'switch'

    def end (self):
        file = open('core/kernel_switchs.h', 'a')
        file.write('}')
        file.close()

        sysinfo.mode = 'inside'

    def endswitch (self):
        file = open('core/kernel.tmp', 'a')
        file.write('}')
        file.close()

    def addnum (self,num,name):
        file = open('core/kernel.tmp', 'a')
        file.write('''
        case {num}:
            _switch_function_{name}_ (\"\");
            break;
        '''
                   .replace('{num}',str(num))
                   .replace('{name}',name)
                   )
        file.close()

    def startdefault (self):
        file = open('core/kernel.tmp', 'a')
        file.write('default:')
        file.close()

    def enddefault (self):
        file = open('core/kernel.tmp', 'a')
        file.write('break;')
        file.close()