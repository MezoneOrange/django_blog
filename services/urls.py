from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="services-main"),
    path('articles/', views.ShowArticlesView.as_view(), name="articles"),
    path('articles/create/', views.CreateNewArticleView.as_view(), name="article-create"),
    path('articles/<int:pk>/', views.ShowArticleDetailView.as_view(), name="article-detail"),
    path('articles/<int:pk>/update/', views.UpdateArticleView.as_view(), name="article-update"),
    path('articles/<int:pk>/delete/', views.DeleteArticleView.as_view(), name="article-delete"),
    path('articles/<str:username>/', views.UserArticlesView.as_view(), name="articles-user"),
    path('uslugi/', views.services, name="services-current"),
]
