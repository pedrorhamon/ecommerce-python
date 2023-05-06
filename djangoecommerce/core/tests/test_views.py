from django.test import TestCase, Client

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

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