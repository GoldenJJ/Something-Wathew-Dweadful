import keyboard

while True:
    if keyboard.is_pressed('r'):
        keyboard.press_and_release('backspace')
        keyboard.write('w')