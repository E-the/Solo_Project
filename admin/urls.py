from django.urls import path
from admin import views

from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    
    # path('message/',views.message),
    path('login/',views.login_page),
    path('main/',views.main),

    path('allusers/', views.user_display),
    path('deleteUser/<int:user_id>', views.delete_user),
    path('changeStatus/<str:username>/', views.change_to_admin),
    path('removeStatus/<str:username>/', views.remove_from_admin),
    path('order',views.order, name="order"),

    path('loginadmin/',views.login_admin),
    path('create/',views.create),    
    path('admin_home/',views.admin_home),
    path('add/',views.add),

    path('edit/<int:id>/', views.edit ,name="edit"),
    path('updatepage/<int:id>', views.updatepage),
    path('delete/<int:id>',views.delete),


    path('contact/',views.contact),
    path('allFeedback/<int:feedback_id>', views.feedback_details),

    path('logout/',views.log_out)

]