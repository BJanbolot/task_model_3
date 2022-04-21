from django.db import models
from django.forms import CharField

# Create your models here.
class Post(models.Model):
    post = CharField(max_length=255)

class Comment(models.Model):
    comment = models.TextField()