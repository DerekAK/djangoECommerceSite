from django.db import models
from django.contrib.contenttypes.models import ContentType # model just like any other model but used to represent generic relationships
from django.contrib.contenttypes.fields import GenericForeignKey # model just like any other model but used to represent generic relationships


# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # question: how can we get information about an object without directly importing from the store app?
    # answer: we need to create a generic way to identify any item in the store app
    # in database terms, a way to identify any item in a database

    # can identify an object based on two attributes
    # content type (product, video, article)
    # object ID

    # ContentType is a model that represents the type of an object in our application
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    
    # the actual object being queried from db
    content_object = GenericForeignKey('content_type', 'object_id')