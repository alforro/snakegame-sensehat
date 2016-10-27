#!/usr/bin/python
import sys
import time
from sense_hat import SenseHat
from evdev import InputDevice, list_devices, ecodes



from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

print("Press Ctrl-C to quit")
time.sleep(1)

x = 3
y = 3

sense = SenseHat()
sense.clear()

snake = []
colour = [255, 0, 255]
snake.append([x,y])
turn = 0

found = False
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
  if dev.name == 'Raspberry Pi Sense HAT Joystick':
    found = True
    break
if not(found):
  print('Raspberry Pi Sense HAT Joystick not found. Aborting ...')
  exit()

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y - 1)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y + 1)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)

def pushed_center(event):
    global turn
    turn = 1
    if event.action != ACTION_RELEASED:
       sense.clear()

def refresh():
    global x,y
    sense.clear()
    snake.append([x,y])
    if len(snake) > 3:
        snake.pop(0)
    for pixel in snake:
        print pixel
        sense.set_pixel(pixel[0], pixel[1], colour)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_center
sense.stick.direction_any = refresh
refresh()
pause()
