from django.db import models

import datetime

# Create your models here.

class TodoModel(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    done = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return "/todolist"


    def __str__(self):
        return self.name
