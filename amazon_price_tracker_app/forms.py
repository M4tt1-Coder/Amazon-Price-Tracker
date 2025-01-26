from django import forms

class urlform(forms.Form):
    user_input=forms.URLField(label="enter URL",initial="https://www.amazon.de/",help_text="here you can enter your url",
                              widget=forms.URLInput(attrs={'class':'bg-blue-500'}))

# TODO - Add all import forms for all user intereactions

# https://www.geeksforgeeks.org/django-forms/
class AddComparisonProductForm(forms.Form): 
    """_summary_

    """
    # the id field to add the product to the comparison list
    product_id = forms.CharField(widget=forms.HiddenInput())  # it's a hidden field, it won't be displayed to the user.
    
    def clean_product_id(self):
        data = self.cleaned_data['product_id']
        
        # make sure the product id is not empty and valid
        if not data:
            raise forms.ValidationError('Product ID is required.')
        
        if len(data) == 0:
            raise forms.ValidationError('The id of a product can not be empty.')
        
        
        
        return data  # return the cleaned data.

# class removeComparisonProductForm(forms.Form):
    