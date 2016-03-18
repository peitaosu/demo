import platform, json, time

code_type = "Undefined"
os = platform.system()
if os == "Windows":
    import keyboard_simulation_win as key
    code_type = "vk_code"
elif os == "Linux":
    import keyboard_simulation_linux as key
    code_type = "key_sym"

with open('./key_mapping.json', 'r') as file:
    code = json.load(file)

def PressKey(key_str):
    key.PressKey(code[key_str][code_type])

def ReleaseKey(key_str):
    key.ReleaseKey(code[key_str][code_type])

def TypeKey(key_str):
    key.PressKey(code[key_str][code_type])
    key.ReleaseKey(code[key_str][code_type])

def test():
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
