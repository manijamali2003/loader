from loader import kernel, io

k = kernel ("MyOwnOs.bin") # Your kernel filename

i = io() # Include VGA Driver in your kernel
i.clear() # Clear the screen
i.println ("Hello World!") # Print Hello World!

k.generate() # Compile your kernel
k.run() # Run your kernel