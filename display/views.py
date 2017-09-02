from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.utils import timezone
# Create your views here.

from .apiget import getLaunchDict
def displaypage(request):
    template_name = 'display/displaypage.html'
    queryset = TodoModel.objects.all()
    # queryset = sorted(queryset, key=queryset.priority)
    # next5LaunchNames, next5LaunchDates = getLaunch5()
    launchDict = getLaunchDict()

    #Get the current week number. TODO: Find a more sleek way to do this..
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    weekNum = datetime.date(year, month, day).isocalendar()[1]

    #TODO check out "Django REST FrameWork

    context = {
        'time': datetime.datetime.now(),
        'todo_list': queryset,
        # 'launchNames': next5LaunchNames,
        # 'launchDates': next5LaunchDates,
        'launchDict': launchDict,
        'weekNum': weekNum,
        'weeksUntilExam': 47 - weekNum,
    }

    return render(request, template_name, context)

from todo.models import TodoModel

def displaypage_cssgrid(request):
    template_name = 'display/displaypage_cssgrid.html'

    queryset = TodoModel.objects.all()
    context = {
        'time': datetime.datetime.now(),
        'todo_object_list': queryset
    }

    return render(request, template_name, context)



def displaypage_cssgridtut(request):
    return render(request, 'display/cssgridtut.html', {})

def displaypage_cssgridtut3(request):
    return render(request, 'display/cssgridtut3.html', {})

def displaypage_cssgridtut4(request):
    return render(request, 'display/cssgridtut4.html', {})
