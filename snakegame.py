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

found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
  if dev.name == 'Raspberry Pi Sense HAT Joystick':
    found = True;
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

def refresh():
    sense.clear()
    sense.set_pixel(x, y, 255, 255, 255)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_any = refresh
refresh()
pause()
