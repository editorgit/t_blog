from datetime import date, timedelta

from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

user_model = get_user_model()


class Writer(models.Model):
    name = models.CharField(max_length=35)
    is_editor = models.BooleanField(default=False)
    user = models.OneToOneField(user_model, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    DRAFT = 'DRA'
    APPROVED = 'APP'
    REJECTED = 'REJ'

    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected')
    ]

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )
    created_at = models.DateTimeField()
    written_by = models.ForeignKey(Writer, related_name='written_by',
                                   on_delete=models.SET_NULL, null=True)
    edited_by = models.ForeignKey(Writer, related_name='edited_by',
                                  on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.title}: {self.status}"

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

    @property
    def is_last_days(self) -> bool:
        days_ago = date.today() - timedelta(days=settings.LAST_DAYS)
        return True if self.created_at > days_ago else False

