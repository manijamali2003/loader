
#include "kernel.h"
void kernel_entry()
{
        init_vga (WHITE,BLACK);init_vga (15,1);print_string("15");init_vga (15,15);print_string("2");init_vga (2,2);print_string("9");init_vga (9,9);print_string("6");init_vga (6,6);print_string("10");init_vga (10,10);print_string("20");}