import urllib.request
import json



def getLaunchDict():
    with urllib.request.urlopen("https://launchlibrary.net/1.2/launch?next=5") as response:
        decodedResponse = response.read().decode('UTF-8')
        pythonDict = json.loads(decodedResponse)
    return pythonDict

#Test
#pythonDict = getLaunchDict()
#How to access:
#print(pythonDict['launches'][1]['name'])