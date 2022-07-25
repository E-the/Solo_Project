from django.test import Client, SimpleTestCase, TestCase
from admin.views import add, updatepage
# from product.models import Item
from app.views import main
from django.contrib.auth.models import User
from django.urls import reverse, resolve

# Create your tests here.
class TestViews(TestCase):

    def test_home(self):

        #create new user with username and password
        user = User.objects.create(username='test12')
        user.set_password('1234')
        user.save()

        # To login 
        client = Client()
        logged_in = client.login(username="test12", password="1234")
        response = client.get(reverse(main))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "main.html")

    def test_product_create_url(self):
        url = reverse("add")
        self.assertEquals(resolve(url).func,add)
    
    def test_product_update_url(self):
          self.assertEqual(
          reverse('updatepage' ,kwargs={'id': "1"}),
          '/admin/updatepage/1')
    
    def test_product_delete_url(self):
        self.assertEqual(
        reverse('delete' ,kwargs={'id': "1"}),
        '/admin/delete/1')

    #  def test_product_product_url(self):
    #     self.assertEqual(
    #     reverse('product' ,kwargs={'id': "1"}),
    #     '/product/product/1')

    

    # def test_add_product(self):
    #     response = self.c.post(reverse('add'),{
    #     "id":"12",
    #     "watch_name": "test_product",
    #     "watch_price": "123",
    #     "watch_detail": "test",
    #     "watch_stock": "ok",
    #     "watch_tec":"description",
    #     "techSpec":"techspec",
    #     "product_catog": "nothing",
    #     "watch_image": "default.jpg",
    #     "watch_image2": "default.jpg",
    #     "watch_image3": "default.jpg",
    #   }) 
    #     self.assertEqual(response.status_code, 302)

    # def test_del_product(self):
    #   response = self.admin.post(reverse('delete', kwargs={'id': 12}),follow=True) 
    #   self.assertEqual(response.status_code, 200) 

    # def test_update_product(self):
    #   response = self.admin.post(reverse('updatepage', kwargs={"id":'30'}),{
    #     "watch_name": "upadted_test_product",
    #     "watch_price": "123",
    #     "watch_detail": "test",
    #     "watch_stock": "ok",
    #     "watch_tec":"description",
    #     "techSpec":"techspec",
    #     "product_catog": "nothing",
    #     "watch_image": "default.jpg",
    #     "watch_image2": "default.jpg",
    #     "watch_image3": "default.jpg",
    #   },follow=True)
    #   self.assertEqual(response.status_code, 302)

