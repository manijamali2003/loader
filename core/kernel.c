
#include "kernel.h"
void __stack_chk_fail(){} void kernel_entry()
{
        init_vga (15,0);init_vga (15,0);print_string("In the name of God, the Compassionate, the Merciful.",15,0);print_new_line(15,0);print_string("Loader Os (c) 2020 Mani Jamali. Free Software GNU General Public License v3.0",15,0);print_new_line(15,0);int _switch_variable_i_ = 0;unsigned long _loop_variable_933746 = 1;while (_loop_variable_933746 <= 1){print_string ("/: ",15,0); _switch_variable_i_ = read_int(15,0);sleep (3);}}