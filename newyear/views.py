import datetime
from datetime import date, timedelta
from django.shortcuts import render

# Create your views here.

def index(request):
    now = date.today()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })

