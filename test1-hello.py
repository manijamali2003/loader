from loader import kernel,vga

k = kernel('MyOwnOs.bin')

## Include driver ##
v = vga()


v.clear() # Clear screen #

v.println('Hello I`m Loader Os written in Python.') # Print this word

## Compile the kernel ##
k.generate()
k.run()