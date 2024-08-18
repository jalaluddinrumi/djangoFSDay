from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#the following variable is called global, which is can access from any where 
#tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value = 0, max_value =5)
    isActive = forms.BooleanField(label="Is Active", required=False)
    #sex = forms.ComboField(label="Gender", fields={0 : "Select Sex", 1 : "Man", 2 : "Women"})



def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasks"]
    })

def add(request):
    # server side validation
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            #tasks.append(task)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/index.html", {
                "form": form
            })


    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })