import os


def playsound():
    # For testing on Windows
    os.startfile('Canucks Hell Yeah Custom.mp3')

# Should work on Raspi but is untested
# os.system('Canucks Hell Yeah Custom.mp3 -q &')