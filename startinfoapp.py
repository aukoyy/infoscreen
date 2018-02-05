import webbrowser
import datetime, time
import os
import sys
import random
from pykeyboard import PyKeyboard
k = PyKeyboard()

def init():
	print('Turning off HDMI...')
	time.sleep(10)
	hdmi_off()
	turn_off_auto_screen_blank()
	prevent_evening_trigger()
	#time.sleep(60*60)
	while True:
		#if weekday, run app (saturday is 5)
		if datetime.datetime.now().weekday() < 5:
			check_time()
		else:
			break
		time.sleep(5)
	#Wake up on saturday nine o clock
	time.sleep(60*60*9)
	start_app()
	success()



#App url
url = 'https://aukinfo.herokuapp.com'


#Input
music_dict = {
	'I need a dollar': 'https://www.youtube.com/watch?v=N8pwUMuS8S0',
	'Toms diner': 'https://www.youtube.com/watch?v=6_x7gTQOEs4',
	'Lanas song': 'https://www.youtube.com/watch?v=oKxuiw3iMBE',
	'Up and away': 'https://www.youtube.com/watch?v=R5xzaDo5Q54',
	'Pisk cotton club': 'https://www.youtube.com/watch?v=Z-xe-sUlREs&list=RDZ-xe-sUlREs&t=9',
	}
def get_random_song_url():
	return random.sample(music_dict.items(), int(1))[0][1]
music_url = music_dict['Pisk cotton club']
#music_url = get_random_song_url()
wake_up_time = int(input('Enter Wake Up Time: '))
shut_down_time = int(input('Enter Shut Down Time: '))
display_is_off = True
#days_running = int(input('Enter how many days to run: '))


# TODO:
# 4. Implement physical button to wake up/ctrl+alt+t + os.system('tvservice -p')
# ~ se knock knock


def turn_off_auto_screen_blank():
	os.system('sudo xset s off')
	os.system('sudo xset -dpms')
	os.system('sudo xset s noblank')


#Time keeping
def now_time():
	now_hour = datetime.datetime.now().hour
	now_min = '%02d' % datetime.datetime.now().minute
	now_time = int(str(now_hour) + str(now_min))
	return now_time


def prevent_evening_trigger():
	print('Preventing evening trigger')
	while now_time() >= shut_down_time:
		time.sleep(10)


#Check if time matches set wake up time
def check_time():
	#print('runnning check_time')
	global display_is_off
	if display_is_off and wake_up_time <= now_time() < shut_down_time:
		print('\n================================================')
		print('waking up')
		start_app()
		time.sleep(20)
		hdmi_on()
		#start_music()
		#time.sleep(60*60*2)
		#stop_music()
	if not display_is_off and now_time() >= shut_down_time:
		close_web()
		print('going to sleep in 10 sek')
		time.sleep(10)
		hdmi_off()


def hdmi_on():
	print('turning monitor on')
	print('time is: ' + str(now_time()))
	os.system("tvservice -p")
	global display_is_off
	display_is_off = False


def start_app():
        webbrowser.get(using='chromium-browser').open(url)
	time.sleep(5)
	k.tap_key(k.function_keys[11])


def start_music():
	webbrowser.get(using='chromium-browser').open(music_url)
	time.sleep(10) #PI is slow
	k.press_key(k.control_l_key)
	k.press_key(k.shift_key)
	time.sleep(2)
	k.tap_key(k.tab_key)
	k.release_key(k.shift_key)
	k.release_key(k.control_l_key)


def stop_music():
	k.press_key(k.control_l_key)
	k.tap_key(k.tab_key)
	time.sleep(1)
	k.tap_key('w')
	k.release_key(k.control_l_key)


def close_web():
	k.press_key(k.control_l_key)
	k.tap_key('w', n=4, interval=3)
	k.release_key(k.control_l_key)


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
