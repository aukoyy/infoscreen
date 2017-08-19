from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.utils import timezone
# Create your views here.

from .apiget import getLaunch5, getLaunchDict
def displaypage(request):
    template_name = 'display/displaypage.html'
    queryset = TodoModel.objects.all()
    # queryset = sorted(queryset, key=queryset.priority)
    # next5LaunchNames, next5LaunchDates = getLaunch5()
    launchDict = getLaunchDict()


    #TODO check out "Django REST FrameWork

    context = {
        'time': datetime.datetime.now(),
        'todo_list': queryset,
        # 'launchNames': next5LaunchNames,
        # 'launchDates': next5LaunchDates,
        'launchDict': launchDict,
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
