from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

with keyboard.pressed(Key.cmd):
	keyboard.press('r')
	keyboard.release('r')
time.sleep(1)




for char in "cmd.exe":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(5)
for char in "cd C:/Users/treve/documents/python-things":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

for char in "./clean.bat":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)


time.sleep(5)
for char in "git add *":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(5)
for char in "git commit -m \"m\" ":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(5)
for char in "git push origin master":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
