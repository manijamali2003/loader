from loader import io, kernel, time, type, color, show_type,vfs, ttychar

k = kernel('loader.bin')

# Drivers #
io = io()
time = time()
fs = vfs()
tty1 = ttychar()

io.clear()

io.println('     In the name of God, the Compassionate, the Merciful')
io.println(' Loader Os v0.1 (c) 2020 Mani Jamali. GNU General Public License')
io.newline()
io.println(' Git source https://github.com/manijamali2003/loader  enter m for see commands')

io.newline()

## TTY 1 ##
tty1.start_timeout = 1
tty1.end_timeout = 1
tty1.prompt = '/: '

tty1.start()
    ## Clear screen command ##
tty1.define('c')
io.clear()
tty1.enddef()
    ##
    ## Reboot ##
tty1.define('r')
k.reboot()
tty1.enddef()
    ##
    ## Version ##
tty1.define('v')
io.println(' Loader Os (c) 2020 Mani Jamali. version 0.1')
tty1.enddef()
    ##
    ## Version ##
tty1.define('h')
io.println(' Hello! I`m Loader kernel written in Python!')
tty1.enddef()
    ##
    ## Version ##
tty1.define('g')
io.println(' Git source https://github.com/manijamali2003/loader')
tty1.enddef()
    ##
    ## Version ##
tty1.define('m')
io.println(' Single charactor TTY1 commands:')
io.newline()
io.println('  c:    Clear screen')
io.println('  r:    Reboot the kernel')
io.println('  v:    About kernel')
io.println('  h:    Sey hello')
io.println('  g:    Show git source')
tty1.enddef()
    ##
tty1.end()

k.generate()
k.run()