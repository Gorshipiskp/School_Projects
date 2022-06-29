from .models import Answers
from django.forms import ModelForm, TextInput, Textarea, IntegerField, NumberInput


class Answersform(ModelForm):
    variants: IntegerField()

    class Meta:
        model = Answers
        fields = ["name", "subject", "variants", "contains", "date", "author", "krypto", "is_checked"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-group',
                "style": "margin-bottom:10px; width: 400px",
                'placeholder': 'Введите название теста'
            }),
            "subject": TextInput(attrs={
                'class': 'form-group',
                "style": "margin-bottom:10px; width: 400px",
                'placeholder': 'Введите предмет'
            }),
            "contains": Textarea(attrs={
                'class': 'form-group',
                "style": "margin-bottom:10px; width: 600px; height: 400px",
                'placeholder': 'Введите содержание (ответы, вопросы и т.д)'
            }),
            "variants": NumberInput(attrs={
                'class': 'form-group',
                "style": "margin-bottom:10px; width: 400px",
                'placeholder': 'Введите количество вариантов'
            })
        }
