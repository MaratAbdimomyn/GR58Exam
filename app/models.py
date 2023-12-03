from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class ToDoList(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default="general", on_delete=models.PROTECT)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title