from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin  # отслеживание авторизованности
from django.contrib.auth.mixins import UserPassesTestMixin  # проверка пользователя
from django.views.generic import ListView  # передача данных из таблицы через класс, вместо функции
from django.views.generic import DetailView  # передача данных из таблицы через класс одного конкретного объекта
from django.views.generic import CreateView  # для создания новых записей в базе данных
from django.views.generic import UpdateView  # для обновления данных
from django.views.generic import DeleteView
from django.core.mail import send_mail

from .models import Service
from .models import Article
from .forms import FeedbackForm


class UserArticlesView(ListView):
    model = Article
    template_name = 'services/user_articles.html'
    context_object_name = 'articles'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(author=user).order_by('-date')

    def get_context_data(self, **kwards):
        # передача доп данных
        context = super(UserArticlesView, self).get_context_data(**kwards)
        context['title'] = f"Все статьи от пользователя {self.kwargs.get('username')}"
        return context


class ShowArticlesView(ListView):
    model = Article
    template_name = 'services/articles.html'
    context_object_name = 'articles'
    ordering = ['-date']
    paginate_by = 4

    def get_context_data(self, **kwards):
        # передача доп данных
        context = super(ShowArticlesView, self).get_context_data(**kwards)
        context['title'] = "Все статьи"
        return context


class ShowArticleDetailView(DetailView):
    # article_detail.html
    model = Article

    def get_context_data(self, **kwards):
        # передача доп данных
        context = super(ShowArticleDetailView, self).get_context_data(**kwards)
        context['title'] = Article.objects.filter(pk=self.kwargs['pk']).first()
        return context


class CreateNewArticleView(LoginRequiredMixin, CreateView):
    # article_form.html
    model = Article
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateNewArticleView, self).form_valid(form)

    def get_context_data(self, **kwards):
        # передача доп данных
        context = super(CreateNewArticleView, self).get_context_data(**kwards)
        context['title'] = "Создание статьи"
        return context


class UpdateArticleView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UpdateArticleView, self).form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

    def get_context_data(self, **kwards):
        # передача доп данных
        context = super(UpdateArticleView, self).get_context_data(**kwards)
        context['title'] = "Обновление статьи"
        return context


class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # article_confirm_delete.html
    model = Article
    success_url = '/articles/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(DeleteArticleView, self).form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

    def get_context_data(self, **kwards):
        # передача доп данных
        context = super(DeleteArticleView, self).get_context_data(**kwards)
        context['title'] = "Удаление статьи"
        return context


def home(request):
    """Main page of the site."""
    data = {
        'title': 'Главная'
    }
    return render(request, "services/home.html", data)


def services(request):
    """Page that shown a services only in Latin"""
    data = {
        'title': 'Услуги',
        'items': Service.objects.all(),
    }
    return render(request, "services/services.html", data)


def send_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['title']
            plain_message = form.cleaned_data['text']
            from_email = form.cleaned_data['email']
            toward = "mezoneorange@gmail.com"

            send_mail(subject, plain_message, from_email, [toward], fail_silently=False)
            messages.success(request, "Сообщение было успешно отправлено")
            return redirect('articles')
    else:
        form = FeedbackForm()
    data = {
        'title': "Обратная связь",
        'form': form,
    }
    return render(request, "services/feedback.html", data)
