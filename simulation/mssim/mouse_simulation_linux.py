from Xlib import X
from Xlib.display import Display
from Xlib.ext.xtest import fake_input

display = Display()

def move(x, y):
    fake_input(display, X.MotionNotify, x, y)

def press(x, y, button=1):
    move(x, y)
    '''
    Redefined right button flag 3 to 2
    '''
    if button == 2:
        button = 3
    fake_input(display, X.ButtonPress, button)

def release(x, y, button=1):
    move(x, y)
    '''
    Redefined right button flag 3 to 2
    '''
    if button == 2:
        button = 3
    fake_input(display, X.ButtonRelease, button)

def click(x, y, button=1):
    move(x, y)
    '''
    Redefined right button flag 3 to 2
    '''
    if button == 2:
        button = 3
    fake_input(display, X.ButtonPress, button)
    fake_input(display, X.ButtonRelease, button)

def dclick(x, y, button=1):
    move(x, y)
    '''
    Redefined right button flag 3 to 2
    '''
    if button == 2:
        button = 3
    fake_input(display, X.ButtonPress, button)
    fake_input(display, X.ButtonRelease, button)

def test():
    # move mouse
    move(100, 100)
    # mouse left press
    press(150, 150, 1)
    # mouse right press
    press(150, 150, 2)
    # mouse left release
    release(150, 150, 1)
    # mouse right release
    release(150, 150, 2)
    # mouse left click
    click(200, 200, 1)
    # mouse right click
    click(200, 200, 2)
    # mouse left double click
    dclick(100, 250, 1)
    # mouse right double click
    dclick(200, 250, 2)
