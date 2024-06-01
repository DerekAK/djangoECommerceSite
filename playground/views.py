from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view function is a request handler or action, but in django its called a view

# first view function
def say_hello(request):
    # pull data from db, transform data, send email, etc.
    # for now, just return simple response
    #return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name': 'Derek'})