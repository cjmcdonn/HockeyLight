import datetime
import time
import os
# import RPi.GPIO
import urllib.request
from bs4 import BeautifulSoup


def getscore():
    team = "Vancouver"
    url = "http://www.nhl.com/ice/scores.htm"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page)

    # Scrapes score from table data out of table matching team name
    team_list = soup.find('a', text=team)
    try:
        for td in team_list.parent.find_next_siblings('td', class_='total'):
            current_score = td.text
            return int(current_score)
    except AttributeError:
        current_score = 998  # 998 indicates the team is not on the schedule for that day
        return int(current_score)


# def flash():
#     def blink(pin):
#             RPi.GPIO.output(pin, RPi.GPIO.HIGH)
#             time.sleep(1)
#             RPi.GPIO.output(pin, RPi.GPIO.LOW)
#             time.sleep(1)
#             return
#
#     # to use Raspberry Pi board pin numbers
#     RPi.GPIO.setmode(RPi.GPIO.BOARD)
#     # set up GPIO output channel
#     RPi.GPIO.setup(11, RPi.GPIO.OUT)
#     # blink GPIO17 50 times
#     for i in range(0, 50):
#             blink(11)
#     RPi.GPIO.cleanup()


def main():
    # Set first oldScore variable
    old_score = 0
    # Set first current hour and month variable
    now = datetime.datetime.now()
    hour = now.hour
    month = now.month

    continuous = True  # Loop to run 24/7/365
    while continuous:
        while month in (7, 8, 9):  # Slow program during off months
            time.sleep(3600)
            now = datetime.datetime.now()
            month = now.month
        while hour < 11:  # Slow program down during off hours
            time.sleep(120)
            now = datetime.datetime.now()
            hour = now.hour
        while 10 < hour:  # Run GetScore from 1100 to 23:59, after 23:59 hour should reset to 0
            new_score = getscore()
            if new_score == 0:
                old_score = new_score
            elif new_score == 999:  # Indicates game hasn't started yet, triggers short sleep - unsupported
                time.sleep(60)
            elif new_score == 998:  # Indicates team is not on schedule,triggers long sleep
                time.sleep(3600)
            elif new_score > old_score:  # Goal has been scored
                # Play sound
                os.startfile('Canucks Hell Yeah Custom.mp3')  # For testing on Windows
                # os.system('Canucks Hell Yeah Custom.mp3 -q &')  # Should work on Raspi but is untested
                # Flash lights
                # flash()  # Should work on Raspi but is untested
                old_score = new_score  # Set oldScore = newScore so we can evaluate for next goal
            now = datetime.datetime.now()  # Update hour while running while loop
            hour = now.hour
            time.sleep(2)  # Slow this dude down a bit

if __name__ == "__main__":
    main()
