import webbrowser
import datetime, time

url = 'https://aukinfo.herokuapp.com/'
url2 = 'https://google.com/'

# chrome_path = 'pwd --> chrome' could be used as .get(chrome_path)

# webbrowser.get(using='google-chrome').open(url)

print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)

def start():
    if datetime.datetime.now().minute > 3:
        print('yey')

# tvservice -o turns off HDMI
# tvservice -p turns on HDMI



var = True

def het():
    global var
    var = False

print(var)
het()
print(var)