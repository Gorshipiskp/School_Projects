from .models import Answers
from django.forms import ModelForm, TextInput, Textarea, BooleanField, IntegerField


class Answersform(ModelForm):
    variants: IntegerField()

    class Meta:
        model = Answers
        fields = ["name", "subject", "variants", "contains", "date", "author", "krypto"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-group',
                "style": "margin-bottom:10px",
                'placeholder': 'Введите название теста'
            }),
            "subject": Textarea(attrs={
                'class': 'form-group',
                "style": "margin-bottom:10px",
                'placeholder': 'Введите предмет'
            }),
            "contains": Textarea(attrs={
                'class': 'form-group',
                "style": "margin-bottom:10px",
                'placeholder': 'Введите содержание (ответы, вопросы и т.д)'
            })
        }
