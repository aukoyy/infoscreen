from django.shortcuts import render
import datetime

from .apiget import getLaunchDict
from .libquotes import get_random_ben_quote
from .bedpressfinder import bedpressFinderApi


def displaypage(request):
    template_name = 'display/displaypage.html'
    all_todo_items = TodoModel.objects.all()
    launchDict = getLaunchDict()
    futureBedpress = bedpressFinderApi()

    #Get the current week number. TODO: Find a more sleek way to do this...
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    weekNum = datetime.date(year, month, day).isocalendar()[1]

    quote_of_the_day = get_random_ben_quote()


    context = {
        'todo_list': all_todo_items,
        'launchDict': launchDict,
        'weekNum': weekNum,
        'weeksUntilExam': 48 - weekNum,
        'ben_quote': quote_of_the_day,
        'bedpresser': futureBedpress,
    }

    return render(request, template_name, context)




# Alternative design:

from todo.models import TodoModel

def displaypage_cssgrid(request):
    template_name = 'display/displaypage_cssgrid.html'

    queryset = TodoModel.objects.all()
    context = {
        'time': datetime.datetime.now(),
        'todo_object_list': queryset
    }

    return render(request, template_name, context)

# CSS Grid Tutorial:

def displaypage_cssgridtut(request):
    return render(request, 'display/cssgridtut.html', {})

def displaypage_cssgridtut3(request):
    return render(request, 'display/cssgridtut3.html', {})

def displaypage_cssgridtut4(request):
    return render(request, 'display/cssgridtut4.html', {})
