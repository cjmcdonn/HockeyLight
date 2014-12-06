import urllib.request
import HockeyLight_Config
from bs4 import BeautifulSoup

#team = HockeyLight_Config.team()

url = "http://scores.nbcsports.com/nhl/scoreboard.asp"
# This works, however is using a set day for testing, will need url changed to url1 for current day scoreboard
#url = "http://scores.nbcsports.com/nhl/scoreboard.asp?day=20141202"
#team = HockeyLight_Config.team()
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page)

# Creates empty list to store the score
score = []
# Scrapes score from table data out of table matching team name
vancouver = soup.find('a', text='Vancouver')
try:
    for td in vancouver.parent.find_next_siblings('td', class_='shsTotD'):
        # Debug
        print(td.text)
        # Adds scores to the list
        score.append(td.text)
    # Debug
except AttributeError:
    print("Exception")
        # currentscore = 998  # 998 indicates the team is not on the schedule for that day
        # #return int(currentscore)
        # # Debug
        # print(currentscore)

# This needs to check if there are any values in list score.
# If there is list score and an exception wasn't thrown and the list is empty, the game hasn't started yet
if not score:
    currentscore = 999  # 999 indicates the game hasn't started yet
    #return int(currentscore)
    # Debug
    print(currentscore)
else:
    print("The current score is", max(score))


# Debug
#for td in score:
#    print(td, "from the list")
#return(max(score))