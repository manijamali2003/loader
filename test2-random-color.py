from loader import kernel,io,time
import random

k = kernel('MyOwnOs.bin')

## Include drivers ##
v = io()   ## VGA Driver
t = time()  ## Time Driver
##

i = 1
while i<=5:
    random_color = random.randint(1,16) # Create random number for colors

    v.color(random_color,random_color)  # Clean the screen with this colors

    t.sleep(2) # Sleep

    i+=1

k.reboot()

## Compile the kernel ##
k.generate()
k.run()