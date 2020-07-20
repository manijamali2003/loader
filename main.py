from loader import kernel, vga, time, address, colors, show_type
import random

k = kernel('kernel.bin')

## Use vga driver in kernel ##
v = vga(); t = time()
v.clear() ## Clear screen

## Show prompt ##

v.clear()
v.show_message('distro',show_type.ok_start,'')
t.sleep(10)
v.println('Hello World!')
k.generate() # Build the kernel ##
k.run() ## Run the kernel ##