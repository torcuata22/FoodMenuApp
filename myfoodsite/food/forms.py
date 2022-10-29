#from socket import fromshare
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    #create metaclass indicating fields that should be present in the form
    class Meta:
        model = Item #model we awnt to use for the form
        fields = ['item_name','item_desc','item_price','item_image'] #fields from model we want to modofy through form
