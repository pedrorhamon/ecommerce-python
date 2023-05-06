from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self):
        pass


    def test_status_code(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')