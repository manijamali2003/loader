
#include "kernel.h"
void __stack_chk_fail(){} void kernel_entry()
{
        init_vga (15,0);init_vga (15,0);
            print_string ("[ ",15,0);
            print_string ("OK",BRIGHT_GREEN,0);
            print_string (" ] ",15,0);
            print_string ("Start distro process.",15,0);
            print_new_line(15,0);
            sleep (10);print_string("Hello World!",15,0);print_new_line(15,0);}