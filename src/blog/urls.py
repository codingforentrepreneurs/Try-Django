from django.urls import path
from .views import (
    ArticleListView   
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    #path('create/', view_name, name='article-create'),
    #path('<int:id>/', view_name, name='article-detail'),
    #path('<int:id>/update/', view_name, name='article-update'),
    #path('<int:id>/delete/', view_name, name='article-delete'),
]