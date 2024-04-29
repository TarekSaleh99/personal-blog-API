from django.urls import path
from .views import ArticleListCreate, ArticleRetrieveUpdateDestroy
urlpatterns = [
    path('articles/', ArticleListCreate.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroy.as_view(), name='article-detail'),
]
