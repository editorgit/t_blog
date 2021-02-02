from django.contrib.auth.decorators import login_required
from django.urls import path

from blog.views import index, ArticleUpdate, article_approval, \
    ArticleEditedListView, ArticleCreate, ArticleListView, \
    update_status

urlpatterns = [
    path('', index, name='index'),
    path('article/new/', login_required(ArticleCreate.as_view()),
         name='article-new'),
    path('article/<int:pk>/', login_required(ArticleUpdate.as_view()),
         name='article-detail'),
    path('article/status/', login_required(update_status),
         name='update-status'),
    path('article/writer/<int:pk>/', ArticleListView.as_view(),
         name='article-writer-list'),
    path('article/approval/', login_required(article_approval),
         name='article-approval'),
    path('article/edited/', login_required(ArticleEditedListView.as_view()),
         name='article-edited'),
]
