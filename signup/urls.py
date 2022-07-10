from django.urls import path
from signup import views

urlpatterns = [
    path("/<int:id>",views.signup),
    path('data/',views.data),
    path("user/",views.user)
    
   
    
    # path('admin/', admin.site.urls),
]
