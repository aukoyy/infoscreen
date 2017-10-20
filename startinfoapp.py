import webbrowser
import datetime, time
import os
import sys


def init():
	while True:
		check_time()
		time.sleep(10)


#App url
url = 'https://aukinfo.herokuapp.com'


#Music urls
urlChillMix = 'https://www.youtube.com/watch?v=R7Y64PvlcI4'
urlTomsDiner = 'https://www.youtube.com/watch?v=6_x7gTQOEs4'
urlDollar = 'https://www.youtube.com/watch?v=N8pwUMuS8S0'
urlLana = 'https://www.youtube.com/watch?v=oKxuiw3iMBE'


#Specifie time for wake up
wakeup_time = 43
shut_down_time = 48


# TODO:
# 1. Take wakeup_time and shut_down_time as input
# 2. Implement PyUserInput and KeyBoardinput with spotify app or web player
	# oooooooor just use KeyBoardinput to f11 chromium and kill it on sleep_time (shut_down_time)
# 4. Implement physical button to wake up/ctrl+alt+t + os.system('tvservice -p')
# ~ se knock knock


#Turn HDMI OFF
print('Turning off HDMI and going to sleep')
print('Start HDMI again by opening a new terminal window (ctrl+alt+t) and type "tvservice -p" + enter')
time.sleep(10)
os.system('tvservice -o')
display_is_off = True


#Remember to suspend rasbians screen blank mode in /etc/ligthdm/lightdm.config
# under [seatDefaults] : xserver-command=X -s 0 -dpms
os.system('sudo xset s off')
os.system('sudo xset -dpms')
os.system('sudo xset s noblank')


#Time keeping
def now_time():
	now_hour = datetime.datetime.now().hour
	now_min = '%02d' % datetime.datetime.now().minute
	now_time = int(str(now_hour) + str(now_min))
	return now_time


#If evening, don't trigger
if now_time() >= shut_down_time:
	print('Preventing evening trigger')
	while now_time() >= shut_down_time:
		time.sleep(10)


#Check if time matches set wake up time
def check_time():
	#print('runnning check_time')
	global display_is_off
	if display_is_off and wakeup_time <= now_time() < shut_down_time:
		print('\n================================================')
		print('waking up')
		hdmi_on()
		start_music()
	if not display_is_off and now_time() >= shut_down_time:
		print('going to sleep in 10 sek')
		time.sleep(10)
		hdmi_off()
		time.sleep(200)
		success()


def hdmi_on():
	print('turning monitor on')
	print('time is: ' + str(now_time()))
	os.system("tvservice -p")
	global display_is_off
	display_is_off = False


def start_music():
	#Open music
	webbrowser.get(using='chromium-browser').open(urlDollar)
	time.sleep(20) #PI is slow
	#Open info app
	webbrowser.get(using='chromium-browser').open(url)


def stop_music():
	pass


def hdmi_off():
	os.system("tvservice -o")
	global display_is_off
	display_is_off = True


def success():
	print('\n================================================')
	os.system("tvservice -p")
	print('success!')
	sys.exit('System exit, app terminated')


if __name__ == "__main__":
	init()
