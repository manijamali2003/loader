from loader import kernel, vga, time
import random

k = kernel('kernel.bin')

## Use vga driver in kernel ##
v = vga()
v.clear() ## Clear screen
v.color(vga.black,vga.green) ## Color blue and white

t = time()

t.startloop(20,1)
v.println('Hello World!')
i = t.counter(-20)
t.endloop()

k.generate() # Build the kernel ##
k.run() ## Run the kernel ##