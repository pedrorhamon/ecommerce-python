from django.test import TestCase, Client

class IndexViewTestCase(TestCase):
    def test_status_code(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(response.status_code, 200)