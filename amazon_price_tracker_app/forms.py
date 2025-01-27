
from django import forms

class urlform(forms.Form):
    user_input=forms.URLField(label="enter URL",initial="https://www.amazon.de/",help_text="here you can enter your url",
                              widget=forms.URLInput(attrs={'class':'bg-blue-500'}))

# https://www.geeksforgeeks.org/django-forms/
class AddComparisonProductForm(forms.Form): 
    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput()) 

