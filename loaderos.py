from loader import io, kernel, time, type, color, show_type,vfs, ttychar

k = kernel('loader.bin')

# Drivers #
io = io()
time = time()
fs = vfs()
tty1 = ttychar()

fs.blocks(1)
fs.addblock(0,'system','getway address')

io.clear()
io.show_message('',show_type.power_on,'')
io.show_message('tty1',show_type.ok_start,'')
io.newline()
tty1.start_timeout = 1
tty1.end_timeout = 1
tty1.prompt = ' /: '
tty1.fgcolor = color.light_cyan
tty1.addr_prompt = 0
tty1.addr_fgcolor = color.light_magenta

tty1.start()

tty1.define('c')
io.clear()
tty1.enddef()

tty1.define('r')
k.reboot()
tty1.enddef()

tty1.define('v')
io.println(' Loader Os (c) 2020 Mani Jamali. version 0.1')
tty1.enddef()

tty1.define('h')
io.println(' Hello! I`m Loader kernel written in Python!')
tty1.enddef()

tty1.define('g')
io.println(' Git source https://github.com/manijamali2003/loader')
tty1.enddef()

tty1.define('m')
io.println(' Single charactor TTY1 commands:')
io.newline()
io.println('  c:    Clear screen')
io.println('  r:    Reboot the kernel')
io.println('  v:    About kernel')
io.println('  h:    Sey hello')
io.println('  g:    Show git source')
tty1.enddef()

tty1.define('k')
io.println(' Kernel Python v0.1')
tty1.enddef()

tty1.end()

k.generate()
k.run()