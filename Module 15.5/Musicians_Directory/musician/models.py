from django.db import models


# Create your models here.


class Musician(models.Model):
    First_Name=models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Phone_numer=models.CharField(max_length=15)
    Instrument_type = models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.First_Name
    

