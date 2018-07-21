import urllib.request
import json

def getLaunchDict():
    with urllib.request.urlopen("https://launchlibrary.net/1.2/launch?next=7") as response:
        decodedResponse = response.read().decode('UTF-8')
        pythonDict = json.loads(decodedResponse)
    return pythonDict
