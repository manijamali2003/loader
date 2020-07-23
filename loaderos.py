from loader import io, kernel, time, type, color, show_type,vfs

k = kernel('loader.bin')

def power_on():
    io.show_message('', show_type.power_on, '')
    time.sleep(2)

def power_off():
    io.show_message('', show_type.power_off, '')
    time.sleep(2)

# Drivers #
io = io()
time = time()
fs = vfs()

io.clear()

fs.defv(type.char,'a')

io.readchar('${a}','Enter your name')
io.showchar('${a}')

k.generate()
k.run()