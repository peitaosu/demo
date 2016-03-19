import ctypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

def move(x, y):
    user32.SetCursorPos(x, y)

def press(x, y, button=1):
    button_action = 2 ** ((2 * button) - 1)
    move(x, y)
    user32.mouse_event(button_action, x, y)

def release(x, y, button=1):
    button_action = 2 ** (2 * button)
    move(x, y)
    user32.mouse_event(button_action, x, y)

def click(x, y, button=1):
    move(x, y)
    button_action = 2 ** ((2 * button) - 1)
    user32.mouse_event(button_action, x, y)
    button_action = 2 ** (2 * button)
    user32.mouse_event(button_action, x, y)

def dclick(x, y, button=1):
    move(x, y)
    button_action = 2 ** ((2 * button) - 1)
    user32.mouse_event(button_action, x, y)
    button_action = 2 ** (2 * button)
    user32.mouse_event(button_action, x, y)
    button_action = 2 ** ((2 * button) - 1)
    user32.mouse_event(button_action, x, y)
    button_action = 2 ** (2 * button)
    user32.mouse_event(button_action, x, y)

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
