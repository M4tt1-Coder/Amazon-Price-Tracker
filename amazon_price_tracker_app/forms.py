from django import forms

class urlform(forms.Form):
    user_input=forms.URLField(label="enter URL",initial="https://fakestoreapi.com/products/",help_text="here you can enter your url",
                              widget=forms.URLInput(attrs={'class':'bg-blue-500 width-800'}))

# https://www.geeksforgeeks.org/django-forms/
# class ModifyProdCmpListForm(forms.Form): 
#     """
#         A form to add a product to the comparison list.
        
#         Validates that the id of the product.
#     """
#     # the id field to add the product to the comparison list
#     action_operation = forms.CharField(widget=forms.HiddenInput(), min_length=7)  # it's a hidden field, it won't be displayed to the user.
    
#     def clean_action_operation(self):
#         print('cleaning action operation')
#         data = self.cleaned_data['action_operation'].split('|')
        
#         product_id = data[0]
#         modify_action = data[1]
        
#         # make sure the product id is not empty and valid
#         if not product_id or not modify_action:
#             raise forms.ValidationError('Product ID is required.')
        
#         if len(data) == 0:
#             raise forms.ValidationError('The id of a product can not be empty.')
        
#         if modify_action in ['ADD', 'DELETE']:
#             raise forms.ValidationError('Invalid action!')
        
#         return data  # return the cleaned data.
