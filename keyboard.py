from pynput.keyboard import Key, Controller
from bs4 import BeautifulSoup
from itertools import tee, islice, chain
import requests
import time

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)
source = requests.get("https://www.google.com/search?q=what%27s+my+ip&rlz=1C1CHBF_enUS806US806&oq=what%27s+my+ip&aqs=chrome..69i57j0l7.5523j1j4&sourceid=chrome&ie=UTF-8").text;

soup = BeautifulSoup(source,'lxml');
thing = soup.findAll("div", {'class': ['BNeawe', 'iBp4i', 'AP7Wnd']});
print(thing[0].text);


keyboard = Controller()

time.sleep(2)
with keyboard.pressed(Key.cmd):
	keyboard.press('r')
	keyboard.release('r')
time.sleep(2)
keyboard.press(Key.enter);
keyboard.release(Key.enter)
time.sleep(5)
for char in "gmail.com":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1);
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(10)
i = 11
while i > 0:
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	time.sleep(.1)
	i = i - 1
time.sleep(3)
keyboard.press(Key.enter)
time.sleep(10)
for char in "trevholm@iu.edu":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)
time.sleep(3)
i = 3
while i > 0:
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	time.sleep(.2)
	i = i - 1
time.sleep(3)
for char in thing[0].text:
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(.1)
time.sleep(1)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
