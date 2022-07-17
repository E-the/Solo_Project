from django.urls import path
from app import views

urlpatterns = [
    path("",views.main),
    path('about/',views.about),
    path('index/',views.index),
    path('gallery/',views.gallery),
    path('footer/',views.footer),
    path('features/',views.features),
    path('checkout/',views.checkout),
    
    path('contact/',views.contact),
    path('create',views.create),
    path("save",views.save),
    path("back",views.back),
    path("edit/<int:id>",views.edit),
    path("update/<int:id>",views.update)
    # path("delete/<int:id>",views.delete)
   
    
    # path('admin/', admin.site.urls),
]
