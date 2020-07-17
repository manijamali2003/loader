
#include "kernel.h"
void kernel_entry()
{
        init_vga (15,0);init_vga (2,0);unsigned long _loop_variable_921 = 20;while (_loop_variable_921 <= 1){print_string("Hello World!",2,0);print_new_line(2,0);_loop_variable_921 = _loop_variable_921 + -20;}}