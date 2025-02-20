from django import forms

class urlform(forms.Form):
    user_input=forms.URLField(label="enter URL",initial="https://fakestoreapi.com/products/",help_text="here you can enter your url",
                              widget=forms.URLInput(attrs={'class':'bg-black width-800 p-2 my-3 rounded-lg text-white'}))
