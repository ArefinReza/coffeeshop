from django.urls import path
from . import views

urlpatterns = [
    path('', views.track_visitor, name='track_visitor'),
]
