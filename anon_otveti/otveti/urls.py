from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create', views.create, name='create'),
    path('submits', views.submits, name='submits')
]
