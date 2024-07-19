from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem

# Create your views here.
# view function is a request handler or action, but in django its called a view

# first view function
def say_hello(request):

    collection = Collection()
    collection.title = "What up baby"
    collection.save() 

    return render(request, 'hello.html', {'name': 'Derek', 'products': list(query_set)})