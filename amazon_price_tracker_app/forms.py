from django import forms

class urlform(forms.Form):
    user_input=forms.CharField(label="enter URL")