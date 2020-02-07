from pynput.keyboard import Key, Controller
import time
import sys

keyboard = Controller()

print("|-------------------------|")
print("|  Which repository would |")
print("|     you like to push?   |")
print("|-------------------------|")
print("| 1) python-things        |")
print("| 2) coolstuff            |")
print("| 3) Chess                |")
print("| 4) Other                |")
print("| 5) Quit                 |")
print("|-------------------------|")
print("")
print(": ",end = '')
userin = input()
print("")
if userin == "1":
	userin = "python-things"
elif userin == "2":
	userin = "coolstuff"
elif userin == "3":
	userin = "Chess"
elif userin == "4":
	print("Enter repository name")
	userin = input()
elif userin == "5":
	sys.exit()

userin =  "cd C:/Users/treve/documents/" + userin
with keyboard.pressed(Key.cmd):
	keyboard.press('r')
	keyboard.release('r')
time.sleep(1)

for char in "cmd.exe":
	keyboard.press(char)
	keyboard.release(char)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(2)
for char in userin:
	keyboard.press(char)
	keyboard.release(char)
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

for char in "clean.bat":
	keyboard.press(char)
	keyboard.release(char)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)



time.sleep(2)
for char in "git pull origin master":
	keyboard.press(char)
	keyboard.release(char)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(2)
for char in "git add *":
	keyboard.press(char)
	keyboard.release(char)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(2)
for char in "git commit -m \"m\" ":
	keyboard.press(char)
	keyboard.release(char)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
for char in "git push origin master":
	keyboard.press(char)
	keyboard.release(char)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
for char in "exit":
	keyboard.press(char)
	keyboard.release(char)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

with keyboard.pressed(Key.alt):
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
