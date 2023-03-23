from django.test import TestCase
from django.http import HttpResponse
from django.db.models import QuerySet
from django.contrib.auth.models import User

from blog.models import Article, Tag


class ListArticlesTestCase(TestCase):
    def get_article_list(self) -> HttpResponse:
        response: HttpResponse = self.client.get("/blog/")
        self.assertIs(response.status_code, 200)

        return response

    def assert_template_name(self, response: HttpResponse):
        template_name: str = response.template_name[0]
        self.assertIn("home.html", template_name)

    def test_list_without_articles(self):
        response: HttpResponse = self.get_article_list()
        self.assert_template_name(response)

        empty_article_list: QuerySet = response.context_data["object_list"]
        self.assertFalse(empty_article_list)

    def test_list_with_articles(self):
        user: User = User.objects.create(username="test_user", password="123")
        tag: Tag = Tag.objects.create(name="test_tag")

        article: Article = Article.objects.create(
            author=user,
            title="test article",
            summary="test summary",
        )
        article.tags.set([tag])

        response: HttpResponse = self.get_article_list()
        self.assert_template_name(response)

        article_list: QuerySet = response.context_data["object_list"]
        self.assertIs(len(article_list), 1)

        for obj in (tag, article, user):
            obj.delete()
