from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('bot/', views.bot_view, name='bot_view'),
]