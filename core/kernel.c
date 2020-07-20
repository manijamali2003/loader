
#include "kernel.h"
#include "kernel_switchs.h"
void __stack_chk_fail(){} void kernel_entry()
{
        init_vga (15,0);int _switch_variable_a_ = 0;print_string ("12*2 = ",15,0); _switch_variable_a_ = read_int(15,0);sleep (2);
        switch (_switch_variable_a_){
        
        case 24:
            _switch_function_answer_ ("");
            break;
        default:print_string("No, it`s 24.",15,0);print_new_line(15,0);break;}}