from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

print("What repository would you like to push?")
userin = input()
userin =  "cd C:/Users/treve/documents/" + userin
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
for char in userin:
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

for char in "clean.bat":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)



time.sleep(5)
for char in "git pull origin master":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)
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
for char in "exit":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)

keyboard.press(Key.enter)
keyboard.release(Key.enter)
