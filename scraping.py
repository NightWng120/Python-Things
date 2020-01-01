from bs4 import BeautifulSoup
import requests

from itertools import tee, islice, chain
def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)
source = requests.get("https://www.google.com/search?q=what%27s+my+ip&rlz=1C1CHBF_enUS806US806&oq=what%27s+my+ip&aqs=chrome..69i57j0l7.5523j1j4&sourceid=chrome&ie=UTF-8").text;

soup = BeautifulSoup(source,'lxml');
for previous, div, nxt in previous_and_next(soup.find_all("div")):
	if div.text == "Your public IP address":
		print(previous.text);
		
