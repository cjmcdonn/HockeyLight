import urllib.request
from bs4 import BeautifulSoup


def getscore():

    url = "http://www.nhl.com/ice/scores.htm"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page)

    # Scrapes score from table data out of table matching team name
    vancouver = soup.find('a', text='Vancouver')
    try:
        for td in vancouver.parent.find_next_siblings('td', class_='total'):
            current_score = td.text
            return int(current_score)
            # Debug
            # print(td.text)
    except AttributeError:
        current_score = 998  # 998 indicates the team is not on the schedule for that day
        return int(current_score)
        # Debug
        # print("Exception 998")
        # print(currentscore)
