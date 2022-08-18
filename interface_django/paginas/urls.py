from django.urls import path
from .views import IndexView


urlpatterns = [
    path('homepage/', IndexView.as_view(), name='homepage')
]