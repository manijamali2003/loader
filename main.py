from loader import kernel, vga

k = kernel('kernel.bin')

## Use vga driver in kernel ##
v = vga()
v.clear() ## Clear screen
v.color(vga.blue,vga.white) ## Color blue and white

i = 1
while i<=100:
    v.print('Hello World!')
    i+=1

k.generate() # Build the kernel ##
k.run() ## Run the kernel ##