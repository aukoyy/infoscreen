import urllib.request
import json



def getLaunch5():
    with urllib.request.urlopen("https://launchlibrary.net/1.2/launch?next=5") as response:
        decodedResponse = response.read().decode('UTF-8')
        pythonDict = json.loads(decodedResponse)

        #Make list of the names
        next5names = []
        for launches in pythonDict["launches"]:
            next5names.append(launches["name"])

        #Make list of the times from net (no earlier than
        next5dates = []
        for dates in pythonDict["launches"]:
            next5dates.append(dates["net"])

    return next5names, next5dates


def getLaunchDict():
    with urllib.request.urlopen("https://launchlibrary.net/1.2/launch?next=5") as response:
        decodedResponse = response.read().decode('UTF-8')
        pythonDict = json.loads(decodedResponse)
    return pythonDict

with urllib.request.urlopen("https://launchlibrary.net/1.2/launch?next=5") as response:
    decodedResponse = response.read().decode('UTF-8')
    pythonDict = json.loads(decodedResponse)

print(pythonDict['launches'][1]['name'])