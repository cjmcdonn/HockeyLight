import datetime
import time
#import HockeyLight.HockeyLight_GetScore
import HockeyLight.HockeyLight_PlaySound
import HockeyLight.HockeyLight_HS
# import HockeyLight.HockeyLight_FlashLight

# SET VARIABLES
# Set first oldScore variable
oldScore = 0
# Set first current hour variable
now = datetime.datetime.now()
hour = now.hour
# Set first current month variable
month = now.month

# Debug
#print(hour, "o'clock hour")
#print(month, "th month")


# MAIN LOOP TO RUN 24/7/365
continuous = True
while continuous:

    # Slow program during off months
    while month in (7, 8, 9):
        # Debug
        print("Sleeping one hour")
        # Sleep program 1 hour then recheck month
        time.sleep(3600)
        now = datetime.datetime.now()
        month = now.month

    # Slow program down during off hours
    while hour < 11:
        # Debug
        print("Sleeping 2 minutes")
        # Sleep program 2 minutes then recheck hour
        time.sleep(120)
        now = datetime.datetime.now()
        hour = now.hour

    # Run GetScore from 1100 to 23:59, after 23:59 hour should reset to 0
    while 10 < hour:
        newScore = HockeyLight.HockeyLight_HS.getscore()
        # Debug
        #print("newScore", newScore)
        #print("oldScore", oldScore)

        # First reset goal oldScore, if score is 0 set oldScore = 0
        if newScore == 0:
            oldScore = newScore
        # This is a 'non-score' probably due to game not having started yet, this triggers a short sleep
        elif newScore == 999:
            # Debug
            #print("newScore was 999 - Game has not yet started - sleep 1 minute")
            time.sleep(60)
        # This is a 'non-score' because the team is not currently on the line-up, this triggers a long sleep
        elif newScore == 998:
            # Debug
            #print("newScore was 998 - Team not on schedule - sleep 1 hour")
            time.sleep(3600)
        # Compare to see if goal has been scored
        elif newScore > oldScore:
            # Play sound and flash light
            HockeyLight.HockeyLight_PlaySound.playsound()
            #HockeyLight_FlashLight
            # Debug
            print("GOAL")
            # Set oldScore = newScore so we can evaluate for next goal
            oldScore = newScore

        # Update hour while running while loop
        now = datetime.datetime.now()
        hour = now.hour
        # Slow this dude down a bit
        time.sleep(5)

