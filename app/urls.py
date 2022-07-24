from django.urls import path
from app import views

urlpatterns = [
    path("",views.main),
    path('about/',views.about),
    path('error/',views.error),
    path('index/',views.index),
    path('gallery/',views.gallery),
    path('footer/',views.footer),
    path('features/',views.features),
    
    path('contact/',views.contact),
    
    
    path("back",views.back),
   
    # path("delete/<int:id>",views.delete)
   
    
    # path('admin/', admin.site.urls),
]
