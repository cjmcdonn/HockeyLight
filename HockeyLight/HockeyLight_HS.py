import urllib.request
import urllib.parse
import re

def getscore():

    team = "Anaheim Ducks"
    urlbase = "https://api.hockeystreams.com/Scores?key="
    apiKey = "4f8eeb0e2a97c856b324b36e5c2ecedc"
    event = "&event=nhl"
    theurl = urlbase + apiKey + event

    # Get response from URL
    resp = urllib.request.urlopen(theurl)
    # Convert to string? Cant do a parse on a urlopen
    see = resp.read().decode('utf-8')

    # Verify team is on schedule for today
    if team in see:
        # The s2 s3 strings cut the string down to only games grouped by {}
        see2 = see[12:]
        see3 = see2[:-3]

        # Split into list by game and remove the outer '{}'
        games = see3.split('},{')
        # Debug
        #print('\n' .join(games))
        #print(len(games))

        # This finds the string s in list games that contains the team
        for s in games:
            if team in str(s):
                # Debug
                #print(s)
                correctGame = s

        # Splits correctGame into list then decide if team is home or away
        gameList = correctGame.split(',')
        # Debug
        #print('\n' .join(gameList))

        # This finds the string s in the list that contains the team
        for s in gameList:
            if team in str(s):
                # Debug
                #print(s)
                # If team is home set home to true
                if "homeTeam" in s:
                    # Debug
                    #print(gameList[7])
                    #score = gameList[7]
                    score = re.findall('\d+', gameList[7])
                    currentScore = ''.join(str(e) for e in score)
                    # Debug
                    #print(currentScore)
                    return int(currentScore)

                # If team is away set home to false
                else:
                    # Debug
                    #print(gameList[12])
                    #score = gameList[12]
                    score = re.findall('\d+', gameList[12])
                    currentScore = ''.join(str(e) for e in score)
                    # Debug
                    #print(currentScore)
                    return int(currentScore)

    # This will return 998 if the Team is not playing that day, triggering a long sleep in Master
    else:
        currentScore = 998
        # Debug
        #print(currentScore)
        return int(currentScore)