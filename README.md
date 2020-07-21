# Loader Module in Python

        In the name of God, the Compassionate, the Merciful
        
    /:oader Os (c) 2020 Mani Jamali. Free Software General Public License v3.0
    
## How to create my own kernel in python
Nowdays you can create your kernel and operating system with Python programing language.
This means that you can deploy you project easily.

 - Requirments
 
 1. Linux i386/amd64, macOS or other unix likes.
 2. Qemu utils
 3. GCC compiler
 4. Python 3
 
 - Create your own kernel starts with `Hello World!`
 
```python
from loader import kernel, io

k = kernel ("MyOwnOs.bin") # Your kernel filename
v = io() # Include VGA Driver in your kernel
v.clear() # Clear the screen
v.println ("Hello World!") # Print Hello World!
k.generate() # Compile your kernel
k.run() # Run your kernel
```