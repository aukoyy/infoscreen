from django.shortcuts import render
import datetime

from .helperfunctions.getLauchDict import getLaunchDict
from .helperfunctions.libquotes import get_random_ben_quote
from .helperfunctions.bedpressfinder import bedpressFinderApi
from .helperfunctions.getCurrentWeek import getCurrentWeek


def displaypage(request):
    template_name = 'display/displaypage.html'

    all_todo_items = TodoModel.objects.all()

    today = datetime.datetime.today()
    quote_of_the_day = get_random_ben_quote()
    weekNum = getCurrentWeek()
    dateToSara = datetime.date(2018, 9, 13)
    launchDict = getLaunchDict()
    futureBedpress = bedpressFinderApi()

    context = {
        'today': today.date(),
        'launchDict': launchDict,
        'weekNum': weekNum,
        'weeksUntilExam': 48 - weekNum,
        'daysToSara': dateToSara - datetime.date.today(),
        'ben_quote': quote_of_the_day,
        'bedpresser': futureBedpress,
    }

    return render(request, template_name, context)




# Alternative design:

from todo.models import TodoModel



