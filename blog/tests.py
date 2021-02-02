from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Article, Writer


USER = 'test_user'
USER_PASS = '12345'


class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title="Foreword",
                               content="Lorem ipsum dolor sit amet. ")

    def test_main_page_is_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_article_default_status(self):
        """Test default status"""
        first = Article.objects.get(title="Foreword")
        self.assertEqual(first.status, 'DRA')

    def test_anonymous_user_published_article(self):
        """Test create article for Anonymous user"""
        title = "Epilogue"
        self.client.post('/article/new/',
                         {'title': title,
                          'content': 'Donec egestas dui a enim vehicula.'})

        self.assertNotEqual(Article.objects.last().title, title)

    def test_logged_user_published_article(self):
        """Test create article for Logged user"""
        user = self.create_user()
        self.create_writer(user)

        logged_in = self.client.login(username=USER, password=USER_PASS)
        self.assertTrue(logged_in)

        title = "Epilogue"
        self.client.post('/article/new/',
                         {'title': title,
                          'content': "Donec egestas dui a enim vehicula."})

        self.assertEqual(Article.objects.last().title, title)

    @staticmethod
    def create_user():
        user = User.objects.create(username=USER)
        user.set_password(USER_PASS)
        user.save()
        return user

    @staticmethod
    def create_writer(user_instance):
        writer = Writer.objects.create(name='writer', user=user_instance)
        return writer
