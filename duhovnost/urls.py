from django.urls import path
from .views import home

app_name = 'duhovnost'

urlpatterns = [
    path('', home, name='home'),
]