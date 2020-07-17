from loader import kernel, vga

k = kernel()
k.set_name('loader.bin')

v = vga()
v.clear()
v.color(vga.blue,vga.white)

k.generate()
k.run()