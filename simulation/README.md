Keyboard & Mouse Simulation
----------------------

# Setup

Xlib and virtkey are the libraries used to send mouse_event and keyboard_event on Linux with X11. So you need to install python-xlib and python-virtkey following the command below here, before use the scripts.:

    sudo apt-get install python-xlib python-virtkey

# Use

Import the package file into your script, call the functions.

Example:

    import kbsim.keyboard_simulation as kb_sim
    import mssim.keyboard_simulation as ms_sim
    
    def run():
        kb_sim.TypeKey("a")
        ms_sim.Click(200, 200, 1)

