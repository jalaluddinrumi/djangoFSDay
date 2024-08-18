from django.urls import path 

from tasks import views

app_name =  "tasks" #this use for name space coliosion
urlpatterns = [

path("", views.index, name="index"),
path("add", views.add, name="add")


]