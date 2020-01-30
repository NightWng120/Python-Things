from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

with keyboard.pressed(Key.cmd):
	keyboard.press('r')
	keyboard.release('r')
time.sleep(3)

for char in "ms-settings:":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)


keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(1)
keyboard.press(Key.tab)
keyboard.release(Key.tab)

time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)


time.sleep(1)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
i = 4
time.sleep(1)
while i > 0:
	keyboard.press(Key.down)
	keyboard.release(Key.down)
	time.sleep(.1)
	i = i - 1
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)


time.sleep(1)
keyboard.press(Key.tab)
keyboard.release(Key.tab)

i = 100
time.sleep(1)
while i > 0:
	keyboard.press(Key.up)
	keyboard.release(Key.up)
	time.sleep(.1)
	i = i - 1
