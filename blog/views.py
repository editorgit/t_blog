from datetime import date, timedelta

from django.conf import settings
from django.db.models import Count, Subquery, IntegerField, Q
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, ListView

from blog.models import Article, Writer


def index(request):
    days_ago = date.today() - timedelta(days=settings.LAST_DAYS)
    context = {
        'writers': Writer.objects.annotate(total_articles=Count('written_by')) \
                                 .annotate(total_30=Count('written_by',
                                                          filter=Q(written_by__created_at__gt=days_ago)))
    }
    return render(request, 'blog/index.html', context=context)


class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.written_by = self.request.user.writer
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.written_by = self.request.user.writer
        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        return super().get_queryset().filter(written_by=self.request.user.writer)


class ArticleEditedListView(ListView):
    model = Article

    def get_queryset(self):
        return super().get_queryset().filter(edited_by=self.request.user.writer)


def article_approval(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'blog/article-approval.html', context=context)


@csrf_exempt
def update_status(request):
    status = request.POST.get('new_status')
    article_id = request.POST.get('article_id')
    editor = request.user.writer
    article = Article.objects.filter(pk=3).update(status=status, edited_by=editor)
    return JsonResponse({
        "result": f"New status: {status}"
    })

