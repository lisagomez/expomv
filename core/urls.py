from django.urls import path
from .views import core_home

app_name = 'core'

urlpatterns = [
    path('', core_home, name="core-home"),
]