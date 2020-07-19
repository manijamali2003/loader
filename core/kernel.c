
#include "kernel.h"
void kernel_entry()
{
        init_vga (15,0);init_vga (15,0);
            print_string ("[ ",15,0);
            print_string ("OK",BRIGHT_GREEN,0);
            print_string (" ] ",15,0);
            print_string ("Start distro process.",15,0);
            print_new_line(15,0);
            char* _address_com_addr_app;_address_com_addr_app= "Loader Os";_address_com_addr_app = "Loader OsHey";print_string(_address_com_addr_app,15,0);}