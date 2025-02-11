from django.urls import path
from .views import signup_view

app_name = 'users'

urlpatterns = [
    path('', signup_view, name='signup'),
]
