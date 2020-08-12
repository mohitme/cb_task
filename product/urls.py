from django.urls import path
from product import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('list', views.list, name='list'),
    path('logout', views.logout, name='logout'),
    path('detail/<int:pk>', views.detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)