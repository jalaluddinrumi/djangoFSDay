from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")
    #return HttpResponse("Hello!")

def jalal(request):
    return HttpResponse("Hi, Jalal")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
    #return HttpResponse(f"Hello, {name.capitalize()} !")