from loader import kernel, vga

k = kernel ("MyOwnOs.bin") # Your kernel filename
v = vga() # Include VGA Driver in your kernel
v.clear() # Clear the screen
v.println ("Hello World!") # Print Hello World!
k.generate() # Compile your kernel
k.run() # Run your kernel