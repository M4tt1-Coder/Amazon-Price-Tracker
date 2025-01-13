from django import forms

class urlform(forms.Form):
    user_input=forms.URLField(label="enter URL",initial="https://www.amazon.de/",help_text="here you can enter your url",
                              widget=forms.URLInput(attrs={'class':''}))