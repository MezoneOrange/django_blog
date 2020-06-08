from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import FeedbackMessage


class FeedbackForm(forms.ModelForm):
    title = forms.CharField(help_text = "Введите тему", error_messages={'required': 'Заполните поле'})
    email = forms.EmailField(help_text = "Введите корректный адресс почты")
    text = forms.CharField(widget=forms.Textarea, help_text = "Введите текст сообщения")

    def __init__(self, *args, **kwards):
        super(FeedbackForm, self).__init__(*args, **kwards)
        self.fields['title'].label = "Тема письма"
        self.fields['email'].label = "Ваша почта"
        self.fields['text'].label = "Текст сообщения"


    class Meta:
        model = FeedbackMessage
        fields = ['title', 'email', 'text']
