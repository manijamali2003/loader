'''
    In the name of God, the Compassionate, the Merciful
    Loader Os (c) 2020 Mani Jamali. All rights reserved
'''

import os,sys,subprocess

class kernel:
    name = ''
    def __init__(self,name):
        self.name = name

        if os.path.isfile('core/kernel.tmp'): os.remove('core/kernel.tmp')

    def generate(self):
        ## kernel.c
        main_start = '''
#include "kernel.h"
void kernel_entry()
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

        ## Link the kernel ##
        link = 'ld -m elf_i386 -T core/linker.ld debug/kernel.o debug/boot.o -o {0} -nostdlib'.replace('{0}', self.name)
        link = link.split(' ')
        subprocess.call(link)

    def run(self):
        ## Run the kernel ##
        subprocess.call(['qemu-system-i386', '-kernel', self.name])

class vga:
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

    ## Clear screen ##
    def clear (self):

        ## Write into kernel ##
        file = open ('core/kernel.tmp','a')
        file.write ('init_vga (WHITE,BLACK);')
        file.close()

    ## Color ##
    def color (self,bg,fg):
        ## Write into kernel ##
        file = open('core/kernel.tmp', 'a')
        file.write('init_vga ({0},{1});'.replace('{0}',str(fg)).replace('{1}',str(bg)))
        file.close()

    ## Print ##
    def print (self,text):
        file = open('core/kernel.tmp', 'a')
        file.write('print_string("'+text+'");')
        file.close()