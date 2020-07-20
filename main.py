from loader import kernel, vga, time, colors, show_type
import random

k = kernel('kernel.bin')

## Use vga driver in kernel ##
v = vga(); t = time()
v.clear() ## Clear screen

## Show prompt ##

v.clear()
v.println('In the name of God, the Compassionate, the Merciful.')
v.println('Loader Os (c) 2020 Mani Jamali. Free Software GNU General Public License v3.0')
k.define('int','i','0')
t.startloop(1,1)
v.inputint('$i','/: ')
t.sleep(3)
t.endloop()

k.generate() # Build the kernel ##
k.run() ## Run the kernel ##