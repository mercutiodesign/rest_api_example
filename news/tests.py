from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from .models import Post


# Test that the REST api has been successfully implemented
class ApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            title="TestTitle", text="TestText", date=timezone.now())

    def setUp(self):
        self.client = Client()

    def test_api_post_list(self):
        response = self.client.get('/api/posts/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # It should return valid JSON
        data = response.json()

        # There should be exactly one post right now
        self.assertEqual(len(data), 1)

        # The post title and text should be correct
        post = data[0]
        expected = ApiTest.post
        self.assertEqual(post['title'], expected.title)
        self.assertEqual(post['text'], expected.text)


# Test that the normal frontend is working as expected
class FrontendTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            title="TestTitle", text="TestText", date=timezone.now())

    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['post_list']), 1)

    def test_post_create(self):
        response = self.client.post(
            reverse('new-post'), {'text': 'new-text', 'title': 'new-title'})
        self.assertRedirects(response, reverse('index'))  # redirect
        self.assertEqual(Post.objects.all().count(), 2)  # created a new post

    def test_invalid_create(self):
        response = self.client.post(
            reverse('new-post'), {'title': 'missing-text'})
        before_count = Post.objects.all().count()
        self.assertEqual(response.status_code, 200)  # show form again
        # hasn't created a new post
        self.assertEqual(Post.objects.all().count(), before_count)
