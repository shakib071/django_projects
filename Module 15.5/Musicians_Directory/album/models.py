from django.db import models
from django.utils import timezone

from musician.models import Musician

# Create your models here.


class Album(models.Model):
    Name = models.CharField(max_length=40)
    musician = models.ForeignKey(Musician,on_delete=models.CASCADE)
    Release_date=models.DateField(default=timezone.now)
    rating_num=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),]
    Rating = models.CharField(max_length=1,choices=rating_num,default='5')


    def __str__(self) -> str:
        return self.Name
    
