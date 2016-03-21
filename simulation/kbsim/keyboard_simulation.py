import os, platform, json, time

code_type = "Undefined"
system = platform.system()
if system == "Windows":
    import keyboard_simulation_win as key
    code_type = "vk_code"
elif system == "Linux":
    import keyboard_simulation_linux as key
    code_type = "key_sym"

with open(os.getcwd()+'/key_mapping.json', 'r') as file:
    code = json.load(file)

def PressKey(key_str):
    key.PressKey(code[key_str][code_type])

def ReleaseKey(key_str):
    key.ReleaseKey(code[key_str][code_type])

def TypeKey(key_str):
    key.PressKey(code[key_str][code_type])
    key.ReleaseKey(code[key_str][code_type])

def test():
    if system == "Windows":
        # Win + R
        PressKey("WIN")
        PressKey("R")
        ReleaseKey("R")
        ReleaseKey("WIN")
        time.sleep(2)
        # C + M + D
        TypeKey("C")
        TypeKey("M")
        TypeKey("D")
        # ENTER
        TypeKey("ENTER")
    elif system == "Linux":
        # Ctrl + Alt + T
        PressKey("CTRL")
        PressKey("ALT")
        PressKey("T")
        ReleaseKey("T")
        ReleaseKey("ALT")
        ReleaseKey("CTRL")
