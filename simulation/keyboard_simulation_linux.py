import virtkey, json, time

# get keysyms code from json file ./keysyms.json
# keysyms code is from https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
with open('./keysyms.json', 'r') as file:
    code = json.load(file)

def PressKey(keysym):
	vk = virtkey.virtkey()
	vk.press_keysym(keysym)


def ReleaseKey(keysym):
	vk = virtkey.virtkey()
	vk.release_keysym(keysym)

def TypeKey(keysym):
	vk = virtkey.virtkey()
	vk.press_keysym(keysym)
	vk.release_keysym(keysym)

if __name__ == "__main__":
	# ctrl + alt + t 
	PressKey(code["Control_L"])
	PressKey(code["Alt_L"])
	PressKey(code["t"])
	ReleaseKey(code["t"])
	ReleaseKey(code["Alt_L"])
	ReleaseKey(code["Control_L"])
	
	time.sleep(2)
	# l + s + enter
	TypeKey(code["l"])
	TypeKey(code["s"])
	TypeKey(code["KP_Enter"])
	
	