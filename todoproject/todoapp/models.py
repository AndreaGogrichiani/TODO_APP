from django.db import models

class Todo(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=200)
