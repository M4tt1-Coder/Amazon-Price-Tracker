from django import forms

class urlform(forms.Form):
    user_input=forms.URLField(label="enter URL",initial="https://www.amazon.de/",
                              widget=forms.URLInput(attrs={'class':'bg-sky-300 rounded'}))