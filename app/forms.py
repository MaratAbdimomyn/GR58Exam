from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('title', 'content', 'created', 'due_date', 'category')