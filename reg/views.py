from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistration
from .forms import ProfileImage
from .forms import UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Пользователь {username} был успешно добавлен!")
            return redirect('services-auth')
    else:
        form = UserRegistration()
    data = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'reg/reg.html', data)


@login_required
def profile(request):
    if request.method == 'POST':
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)
        if img_profile.is_valid() and update_user.is_valid():
            img_profile.save()
            update_user.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('services-profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)
    data = {
        'title': 'Личный кабинет',
        'img_profile': img_profile,
        'update_user': update_user,
    }
    return render(request, 'reg/profile.html', data)
