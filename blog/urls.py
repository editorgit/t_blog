from django.conf.urls import include
from django.urls import path

from blog.views import index, ArticleUpdate, article_approval, ArticleEditedListView, ArticleCreate, ArticleListView, \
    update_status

urlpatterns = [
    path('', index, name='index'),
    path('article/new/', ArticleCreate.as_view(), name='article-new'),
    path('article/<int:pk>/', ArticleUpdate.as_view(), name='article-detail'),
    path('article/status/', update_status, name='update-status'),
    path('article/writer/<int:pk>/', ArticleListView.as_view(), name='article-writer-list'),
    path('article/approval/', article_approval, name='article-approval'),
    path('article/edited/', ArticleEditedListView.as_view(), name='article-edited'),
]
