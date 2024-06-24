from django.db import models
# import datetime
from category.models import Category

# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length=30)
    task_discription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_Assign_Date = models.DateField()
    category = models.ManyToManyField(Category)


    def __str__(self) -> str:
        if self.is_completed is True:
            return f'{self.task_title} -> Completed'
        else :
            return f'{self.task_title} -> not Completed'
