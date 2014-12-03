import os
import HockeyLight_Config

def playsound():
    # For testing on Windows
    os.startfile(HockeyLight_Config.sound())
    # os.startfile('HQ EA Vancouver.mp3')


# Should work on Raspi
#os.system(HockeyLight_Config.sound() -q &')




