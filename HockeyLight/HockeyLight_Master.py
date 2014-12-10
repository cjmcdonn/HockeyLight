import datetime
import time
# from time import strftime
import HockeyLight.HockeyLight_PlaySound
import HockeyLight.HockeyLight_GetScoreNHLcom
# import HockeyLight.HockeyLight_FlashLight


# Set first oldScore variable
old_score = 0
# Set first current hour and month variable
now = datetime.datetime.now()
hour = now.hour
month = now.month

# Loop to run 24/7/365
continuous = True
while continuous:

    # Slow program during off months
    while month in (7, 8, 9):
        # Debug
        # print("Sleeping one hour")
        # print("<----------",strftime("%H:%M:%S"),"---------->", '\n')
        # Sleep program 1 hour then recheck month
        time.sleep(3600)
        now = datetime.datetime.now()
        month = now.month

    # Slow program down during off hours
    while hour < 11:
        # Debug
        # print("Sleeping 2 minutes",)
        # print("<----------",strftime("%H:%M:%S"),"---------->", '\n')
        # Sleep program 2 minutes then recheck hour
        time.sleep(120)
        now = datetime.datetime.now()
        hour = now.hour

    # Run GetScore from 1100 to 23:59, after 23:59 hour should reset to 0
    while 10 < hour:
        new_score = HockeyLight.HockeyLight_GetScoreNHLcom.getscore()
        # Debug
        # print("newScore", new_score)
        # print("oldScore", old_score)
        # print("<----------",strftime("%H:%M:%S"),"---------->", '\n')

        # First reset goal oldScore, if score is 0 set oldScore = 0
        if new_score == 0:
            old_score = new_score
        # This is a 'non-score' probably due to game not having started yet, this triggers a short sleep
        # Currently HockeyLight_GetScoreNHLcom.py does not support this feature
        elif new_score == 999:
            # Debug
            # print("newScore was 999 - Game has not yet started - sleep 1 minute")
            # print("<----------",strftime("%H:%M:%S"),"---------->", '\n')
            time.sleep(60)
        # This is a 'non-score' because the team is not currently on the line-up, this triggers a long sleep
        elif new_score == 998:
            # Debug
            # print("newScore was 998 - Team not on schedule - sleep 1 hour")
            # print("<----------",strftime("%H:%M:%S"),"---------->", '\n')
            time.sleep(3600)
        # Compare to see if goal has been scored
        elif new_score > old_score:
            # Play sound and flash light
            HockeyLight.HockeyLight_PlaySound.playsound()
            # HockeyLight_FlashLight
            # Debug
            # print("GOAL")
            # print("<----------",strftime("%H:%M:%S"),"---------->", '\n')
            # Set oldScore = newScore so we can evaluate for next goal
            old_score = new_score

        # Update hour while running while loop
        now = datetime.datetime.now()
        hour = now.hour
        # Slow this dude down a bit
        time.sleep(2)

