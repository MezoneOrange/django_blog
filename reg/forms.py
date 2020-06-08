from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegistration(UserCreationForm):
    """modified registration form"""
    email = forms.EmailField(required=True)

    class Meta:
        """options for table"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # sequence of fields


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['image'].label = "Изображение профиля"
        self.fields['sex'].label = "Выберите пол"
        self.fields['notice'].label = "Соглашение на отправку уведомлений на почту"

    class Meta:
        model = Profile
        fields = ['image', 'sex', 'notice']
