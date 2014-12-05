import urllib.request
import re
from bs4 import BeautifulSoup

#http://www.nbcsports.com/nhl
#url = "http://scores.nbcsports.msnbc.com/nhl/teamstats.asp?teamno=22&type=teamhome"
url1 = "http://scores.nbcsports.com/nhl/scoreboard.asp"

## This works, however is using a set day for testing, will need url changed to url1 for current day scoreboard
#url = "http://scores.nbcsports.com/nhl/scoreboard.asp?day=20141202"
page = urllib.request.urlopen(url1)
soup = BeautifulSoup(page)

vancouver = soup.find('a', text='Vancouver')
for td in vancouver.parent.find_next_siblings('td', class_='shsTotD'):
    print(td.text)