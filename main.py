from loader import kernel, vga
import random

k = kernel('kernel.bin')

## Use vga driver in kernel ##
v = vga()
v.clear() ## Clear screen
v.color(vga.blue,vga.white) ## Color blue and white

while True:
    i = random.randint(1,20)
    v.print(str(i))
    if i==20: break
    v.color(i,i)

k.generate() # Build the kernel ##
k.run() ## Run the kernel ##