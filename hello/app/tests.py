from django.http import HttpRequest
from django.test import TestCase
from app.views import hello, length


# Create your tests here.

class HelloTestCase(TestCase):
    def test_hello(self):
        request = HttpRequest()
        request.path = ''
        response = hello(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello")

    def test_length(self):
        request = HttpRequest()
        request.path = 'length/'
        request.GET['str'] = "строка"

        response = length(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"6")

    def test_length_no_str(self):
        request = HttpRequest()
        request.path = "length/"

        response = length(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'No input string')