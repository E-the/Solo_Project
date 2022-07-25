from django.test import TestCase
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from app.views import about, error, gallery, footer, contact

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_about_url(self):
        url = reverse(about)
        print(url)
        self.assertEquals(resolve(url).func,about)

    def test_error_url(self):
        url = reverse(error)
        print(url)
        self.assertEquals(resolve(url).func,error)

    def test_gallery_url(self):
        url = reverse(gallery)
        print(url)
        self.assertEquals(resolve(url).func,gallery)
    
    def test_footer_url(self):
        url = reverse(footer)
        print(url)
        self.assertEquals(resolve(url).func,footer)

    def test_contact_url(self):
        url = reverse(contact)
        print(url)
        self.assertEquals(resolve(url).func,contact)