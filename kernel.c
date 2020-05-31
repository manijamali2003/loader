#include "kernel.h"

void kmain()
{
   init_vga(WHITE, BLACK);

   print_string ("Loader Os (c) 2020 Mani Jamali. Free Software GNU General Public License v3.0");
   print_new_line();
   print_new_line();

   while (1)
   {
       sleep(2);
       print_string ("LO1> ");
       read_int();
   }
}

