
#include "kernel.h"
#include "kernel_switchs.h"
void __stack_chk_fail(){} void kernel_entry()
{
        init_vga (15,0);print_string("Hello World!",15,0);print_new_line(15,0);}