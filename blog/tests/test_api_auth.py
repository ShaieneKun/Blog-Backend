from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse


class BlogApiAuthTestCase(TestCase):

    def test_api_get(self):
        api_url: str = reverse("blog_api")
        response: HttpResponse = self.client.get(api_url)
        self.assertIs(response.status_code, 200)