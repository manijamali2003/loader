
#include "kernel.h"
void __stack_chk_fail(){} void kernel_entry()
{
unsigned long _ki = 0;
char* _kchar = "";
        unsigned long blocks = 1;char* addr[] = {"",};char* data[] = {"",};
        addr[0]="system";
        data[0]="getway address";
        init_vga (15,0);
                        print_string ("[ ",15,0);
                        print_string ("OK",BRIGHT_GREEN,0);
                        print_string (" ] ",15,0);
                        print_string ("Power on the kernel.",15,0);
                        print_new_line(15,0);
                        
            print_string ("[ ",15,0);
            print_string ("OK",BRIGHT_GREEN,0);
            print_string (" ] ",15,0);
            print_string ("Start tty1 process.",15,0);
            print_new_line(15,0);
            print_new_line(15,0);while (1){sleep (1);print_string (addr[0],13,0);print_string (" /: ",11,0);char _vfs_kvariable_cmd_ = read_char (11,0);switch (_vfs_kvariable_cmd_){case 'c':init_vga (15,0);break;case 'r':reboot();break;case 'v':print_string(" Loader Os (c) 2020 Mani Jamali. version 0.1",15,0);print_new_line(15,0);break;case 'h':print_string(" Hello! I`m Loader kernel written in Python!",15,0);print_new_line(15,0);break;case 'g':print_string(" Git source https://github.com/manijamali2003/loader",15,0);print_new_line(15,0);break;case 'm':print_string(" Single charactor TTY1 commands:",15,0);print_new_line(15,0);print_new_line(15,0);print_string("  c:    Clear screen",15,0);print_new_line(15,0);print_string("  r:    Reboot the kernel",15,0);print_new_line(15,0);print_string("  v:    About kernel",15,0);print_new_line(15,0);print_string("  h:    Sey hello",15,0);print_new_line(15,0);print_string("  g:    Show git source",15,0);print_new_line(15,0);break;case 'k':print_string(" Kernel Python v0.1",15,0);print_new_line(15,0);break;}sleep(1);}}