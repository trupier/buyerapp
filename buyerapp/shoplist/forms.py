from django import forms
from django.forms import ModelForm
from .models import Item

class AddItemForm(ModelForm):
    item_name = forms.CharField(max_length=200, widget=forms.Textarea(attrs={"placeholder": "Add your item here",}))
    class Meta:
        model = Item
        fields = ["item_name", "amount", "shoplist"]
