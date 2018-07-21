from django.shortcuts import render
import datetime

from .models import QuoteModel
from .helperfunctions.getLauchDict import getLaunchDict
from .helperfunctions.bedpressfinder import bedpressFinderApi
from .helperfunctions.getCurrentWeek import getCurrentWeek


def displaypage(request):
    template_name = 'display/displaypage.html'

    today = datetime.datetime.today()
    weekNum = getCurrentWeek()
    daysToSara = datetime.date(2018, 9, 13) - datetime.date.today()
    oneRandomQuote = QuoteModel.objects.all().order_by('?').first()

    context = {
        'today': today.date(),
        'launchDict': getLaunchDict(),
        'weekNum': weekNum,
        'weeksUntilExam': 48 - weekNum,
        'daysToSara': daysToSara,
        'quote': oneRandomQuote,
        'bedpresser': bedpressFinderApi(),
    }

    return render(request, template_name, context)



