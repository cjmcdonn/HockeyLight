import datetime
import time
import subprocess
# import RPi.GPIO as GPIO
import urllib.request
from bs4 import BeautifulSoup


def get_score(team):
    """
    Return the score of the selected team.

    team = "Team_City"
    The script is configured to work with www.nhl.com/ice/scores.htm
    and will need to be modified if other URLs are used.
    text=team scrapes the table containing the desired team.
    class_='total' selects the cell holding the total score.
    If the given team is not on the schedule to play 998 will be returned.
    """

    #url = "http://www.nhl.com/ice/scores.htm?date=12/22/2014&season=20142015"
    url = "http://www.nhl.com/ice/scores.htm"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page)
    team_list = soup.find('a', text=team)
    try:
        for td in team_list.parent.find_next_siblings('td', class_='total'):
            current_score = td.text
            return int(current_score)
    except AttributeError:
        current_score = 998
        return int(current_score)


# def blink(num_times, pin, speed):
#     GPIO.setmode(GPIO.BOARD)  # Use board pin numbering
#     GPIO.setup(pin, GPIO.OUT)  # Setup GPIO Pin to OUT
#     for i in range(0,num_times):  # Run loop numTimes
#         GPIO.output(pin, True)  # Switch on pin 7
#         time.sleep(speed)
#         GPIO.output(pin, False)  # Switch off pin 7
#         time.sleep(speed)
#     GPIO.cleanup()


def main():
    """
    Alert when a goal is scored by a specified team.

    While in the off-season update the month every hour.
    In-season but outside of any game times check the hour every 2 minutes.
    During potential game times run get_score() and then wait 2 seconds before
    restarting the loop.

    If get_score() returns 0 there has not been a goal in the game so it is
    safe to reset old_score to 0.
    If get_score() returns 998 then the desired team is not on the schedule
    and the loop will wait one hour before restarting.
    If get_score() returns a reasonable score greater than old_score it will
    indicate a goal has been scored, triggering the sound and light and
    setting old_score equal to new_score.
    """

    # Set first old_score variable
    old_score = 0
    # Set first current hour and month variable
    now = datetime.datetime.now()
    hour = now.hour
    month = now.month

    continuous = True  # Loop to run 24/7/365
    while continuous:
        while month in (7, 8, 9):
            time.sleep(3600)
            now = datetime.datetime.now()
            month = now.month
        while hour < 11:
            time.sleep(120)
            now = datetime.datetime.now()
            hour = now.hour
        while 10 < hour:
            new_score = get_score("Vancouver")
            print(new_score)
            if new_score == 0:
                old_score = new_score
            elif new_score == 999:  # Game hasn't started - unsupported
                time.sleep(15)
            elif new_score == 998:  # Team not on schedule
                time.sleep(3600)
            elif new_score > old_score:  # Goal has been scored
                print('GOAL!')
                # Play sound
                #os.startfile('Canucks Hell Yeah Custom.mp3')  # Windows
                #subprocess.call(['omxplayer', 'CanucksHellYeah.mp3'])  # Raspi
                subprocess.call(
                    ['cvlc','CanucksHellYeah.mp3', '--play-and-exit']
                    )  # Linux
                # Flash lights
                # blink(50, 11, 1)  # Should work on Raspi but is untested
                old_score = new_score  # So we can evaluate for next goal
            now = datetime.datetime.now()  # Update hour inside of loop
            hour = now.hour
            time.sleep(2)  # Slow this dude down a bit

if __name__ == "__main__":
    main()
