from django import forms 
  
# https://www.geeksforgeeks.org/django-forms/
class AddComparisonProductForm(forms.Form): 
    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput()) 