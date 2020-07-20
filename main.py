from loader import kernel, vga, time, colors, show_type,switch
import random

k = kernel('loader.pyc')

## Use vga driver in kernel ##
v = vga(); t = time(); s = switch()
v.clear() ## Clear screen

## Show prompt ##

v.clear()
v.println('             In the name of God, the Compassionate, the Merciful.')
v.println('                        /:oader Os (c) 2020 Mani Jamali')
v.newline()

## Commands ##
s.start('hello')
v.println('Hello World!')
s.end()

s.start('clear')
v.clear()
s.end()

s.start('ver')
v.println('Loader Os v0.0.1 (written in Python/C/Assembly)')
s.end()

s.start('help')
v.println('Commands in Loader 0.0.1:')
v.println('    1:   Hello World')
v.println('    2:   Clear Screen')
v.println('    3:   Version information')
v.println('    4:   Help command')
s.end()

## Shell process ##
k.define('int','i','0')
t.startloop(1,1)
v.inputint('$i','/: ')
t.sleep(2)

## Start switch process ##
s.startswitch('$i')
    ## Hello command set ##
s.addnum(1,'hello')

    ## Clear command ##
s.addnum(2,'clear')

    ## Ver command ##
s.addnum(3,'ver')

s.addnum(4,'help')

t.sleep(2)

s.endswitch()
t.endloop()

k.generate() # Build the kernel ##
k.run() ## Run the kernel ##