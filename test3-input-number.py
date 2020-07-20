from loader import kernel,vga,switch,time

k = kernel('MyOwnOs.bin')

## Include driver ##
v = vga()
s = switch()
t = time()

v.clear() # Clear screen #

k.define('int','a','0') # Define a variable in kernel

## Input variables ##
v.inputint('$a','12*2 = ')
t.sleep(2) ## Sleep

## This answer ##
s.start('answer')                  ## function answer for switch
v.println('Yes, it`s correct.')
s.end()                            ## End this function in kernel

## Switch process ##
s.startswitch('$a')
s.addnum(24,'answer')              ## Link to this function
s.startdefault()
v.println('No, it`s 24.')
s.enddefault()
s.endswitch()

## Compile the kernel ##
k.generate()
k.run()