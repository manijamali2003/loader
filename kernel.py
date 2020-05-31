# This is my kernel written in python #
def hello ():
    print_string ("Hello and Welcome to my kernel written in Python")

def kmain ():
    init_vga(WHITE, BLACK)
    hello()
