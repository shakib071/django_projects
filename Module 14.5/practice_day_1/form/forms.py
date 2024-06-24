from django import forms 
from django.forms.widgets import NumberInput
import datetime

class Forms(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment2= forms.CharField(widget=forms.Textarea(attrs={'rows' : 3}))
    email = forms.EmailField()
    agree= forms.BooleanField()
    date = forms.DateField()
    birth_date= forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_address= forms.EmailField(required= False, label="Please enter your email address")
    message = forms.CharField(max_length=10)
    first_name = forms.CharField(initial='Your Name')
    agree2 = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [('blue', 'Blue'),('green', 'Green'),('black', 'Black'),]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())
    

