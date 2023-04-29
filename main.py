# allows for importing of needed libaries
import sys
import subprocess


# download libaries needed
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput'])

from pynput.keyboard import Controller, Listener, Key, KeyCode       # imports keyboard listening and the keyboard controller

number_1 = {Key.tab, KeyCode(char='-')}
number_2 = {Key.tab, KeyCode(char='=')}
ex_mark = {Key.tab, Key.shift, KeyCode(char='_')}
at_key = {Key.tab, Key.shift, KeyCode(char='+')}

combos = [number_1, number_2, ex_mark, at_key]

curr = set()

keyboard = Controller()

def execute(num):
    global curr
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    if num == 0:
        keyboard.press('1')
        keyboard.release('1')
    elif num == 1: 
        keyboard.press('2')
        keyboard.release('2')
    elif num == 2:
        keyboard.press('!')
        keyboard.release('!')
    elif num == 3:
        keyboard.press('@')
        keyboard.release('@')

def on_press(key):
    global curr
    if key == Key.esc:
        curr = set()
        return
    curr.add(key)
    print(curr)
    for num, z in enumerate(combos):
        if len(z) != len(curr):
            continue
        if z == curr:
            execute(num)
      
def on_release(key):
    global curr
    try:
        curr.remove(key)
    except:
        pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

