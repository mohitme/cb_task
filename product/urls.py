from django.urls import path
from product import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('list', views.list, name='list')
]