from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='bce-home'),
    path('about/', views.about, name='bce-about'),
    path('block/<str:block>/', views.block, name='block-info'),
]