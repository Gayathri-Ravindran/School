from . import views
from django.urls import path
app_name = 'finalapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('new_pae/',views.new_page,name='new_page'),
    path('order_form/',views.order_form,name='order_form')
]