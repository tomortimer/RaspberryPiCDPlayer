import gpiod
import subprocess
import keyboard
import time

button = 27
eject = 17
play = 22
chip = gpiod.Chip('gpiochip4')


button_line = chip.get_line(button)
eject_line = chip.get_line(eject)
play_line = chip.get_line(play)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
eject_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
play_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
started = False

# automatically runs play code, hopefully this fixes double button press issue
keyboard.write('bash cdautoplay')
time.sleep(1)
keyboard.send('enter')
time.sleep(1)

while True:
    button_state = button_line.get_value()
    eject_state = eject_line.get_value()
    play_state = play_line.get_value()
    if button_state == 1:
        print("Start button pressed")
        keyboard.write('bash cdautoplay')
        time.sleep(1)
        keyboard.send('enter')
        started = True
        time.sleep(1)
    elif eject_state == 1:
        print("Eject button pressed")
        keyboard.press_and_release('q')
        time.sleep(1)
        started = False
    elif play_state == 1:
        print("Play button pressed")
        keyboard.press_and_release('space')
        time.sleep(1)
