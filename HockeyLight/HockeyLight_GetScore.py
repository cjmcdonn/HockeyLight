import urllib.request
import urllib.parse
import HockeyLight_Config


def getscore():

    # Pull variables from HockeyLight_Config
    theurl = HockeyLight_Config.theurl()
    team = HockeyLight_Config.team()

    # GET INFO AND CLEAN IT UP
    # Get response from URL
    resp = urllib.request.urlopen(theurl)
    # Debug
    #print(resp)
    # Convert to string? Cant do a parse on a urlopen
    s = resp.read().decode('utf-8')
    # Strips most of URL gibberish, probably not needed, artifact from trial and error
    see = urllib.parse.unquote(s)
    # Debug
    #print(see)

    # Verify team is in see
    if team in see:
        # Find location of team in see
        scoreindex = see.find(team)
        # Find location of score after Team
        scorelocation = scoreindex+len(team)+1
        # Set currentscore variable to allow writing to txt file
        currentscore = see[scorelocation]
        # Debug
        #print(see[scorelocation])
        #print(currentscore, "<-- score before verifying it's an integer")

        # Return an int for _Master to compare
        # First verify currentscore is an int, otherwise return 999 (impossible hockey score)
        try:
            int(currentscore)
            return int(currentscore)
        except TypeError:
            currentscore = 999
            return int(currentscore)
    # This will return 998 if the Team is not playing that day, triggering a long sleep in Master
    else:
        currentscore = 998
        return int(currentscore)