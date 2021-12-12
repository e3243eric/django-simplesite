from django.urls import path
from . import views

from django.conf.urls import include
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('allauth.urls')),
]