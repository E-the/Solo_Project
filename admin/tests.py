from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from admin.views import login_page, feedback_details, admin_home, contact, login_admin, order, user_display, login_page, feedback_details
from django.contrib.auth import get_user_model
from app.views import about, main
from product.views import order as orderPr

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_login_page_url(self):
        url = reverse(login_page)
        print(url)
        self.assertEquals(resolve(url).func,login_page)

    def test_contact_url(self):
        url = reverse(contact)
        print(url)
        self.assertEquals(resolve(url).func,contact)

    def test_admin_home_url(self):
        url = reverse(admin_home)
        print(url)
        self.assertEquals(resolve(url).func,admin_home)

    
    
    def test_admin_home_Render(self):
        url = reverse(admin_home)
        print(url)
        self.assertEquals(resolve(url).func,admin_home)

User = get_user_model
class TestViews(TestCase):

    def test_admin_home_Render12(self):
        url = reverse(admin_home)
        response= self.assertEquals(resolve(url).func,admin_home)
        self.assertTemplateUsed(response, "admin/adminhome.html")
    
    
    def test_order(self):
        url = reverse(order)
        response= self.assertEquals(resolve(url).func,order)
        self.assertTemplateUsed(response, "admin/userorder.html")
    

    def test_user_display(self):
        url = reverse(user_display)
        response= self.assertEquals(resolve(url).func,user_display)
        self.assertTemplateUsed(response, 'admin/allusers.html')

      
    def test_admin_login(self):
        url = reverse(login_page)
        response= self.assertEquals(resolve(url).func,login_page)
        self.assertTemplateUsed(response, 'admin/admin_login.html')
    
          
    def test_contact(self):
        url = reverse(contact)
        response= self.assertEquals(resolve(url).func,contact)
        self.assertTemplateUsed(response, 'admin/admin_contact.html')
        
           
    def test_about(self):
        url = reverse(about)
        response= self.assertEquals(resolve(url).func,about)
        self.assertTemplateUsed(response, 'about.html')

          
    def test_main(self):
        url = reverse(main)
        response= self.assertEquals(resolve(url).func,main)
        self.assertTemplateUsed(response, 'main.html')

           
    def test_main(self):
        url = reverse(main)
        response= self.assertEquals(resolve(url).func,main)
        self.assertTemplateUsed(response, 'main.html')


    def test_product(self):
        url = reverse(orderPr)
        response= self.assertEquals(resolve(url).func,orderPr)
        self.assertTemplateUsed(response, 'checkout.html')
    






