
#include "kernel.h"
#include "kernel_switchs.h"
void __stack_chk_fail(){} void kernel_entry()
{
        init_vga (15,0);init_vga (15,0);print_string("             In the name of God, the Compassionate, the Merciful.",15,0);print_new_line(15,0);print_string("                        /:oader Os (c) 2020 Mani Jamali",15,0);print_new_line(15,0);print_new_line(15,0);int _switch_variable_i_ = 0;unsigned long _loop_variable_736966 = 1;while (_loop_variable_736966 <= 1){print_string ("/: ",15,0); _switch_variable_i_ = read_int(15,0);sleep (2);
        switch (_switch_variable_i_){
        
        case 1:
            _switch_function_hello_ ("");
            break;
        
        case 2:
            _switch_function_clear_ ("");
            break;
        
        case 3:
            _switch_function_ver_ ("");
            break;
        
        case 4:
            _switch_function_help_ ("");
            break;
        sleep (2);}}}