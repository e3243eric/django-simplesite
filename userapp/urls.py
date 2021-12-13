from django.urls import path
from . import views
from django.conf.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='accounts/login/')),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('allauth.urls')),
]