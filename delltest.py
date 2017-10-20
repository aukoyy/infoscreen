import datetime, time
import sys


def now_time():
    now_hour = '%02d' % datetime.datetime.now().hour
    print(now_hour)
    now_min = '%02d' % datetime.datetime.now().minute
    now_time = int(str(now_hour) + str(now_min))
    return now_time

#tvservice -p


print(now_time())
print('now_time() is type: ' + str(type(now_time())))
print(now_time() < 2000)