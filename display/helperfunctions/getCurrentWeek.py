import datetime

def getCurrentWeek():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    weekNum = datetime.date(year, month, day).isocalendar()[1]
    return weekNum
