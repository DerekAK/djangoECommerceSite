from django.urls import path
from . import views

# URLConf (URL Configuration) module
# needs to be called urlpatters all lowercase bc django looks for this
urlpatterns = [
    path('hello/', views.say_hello)
]