from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label="Название")
    content = forms.CharField(label="Тект", required=False)
    is_published = forms.BooleanField(label="Опубликовано?", initial=True)
    catagory = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория")