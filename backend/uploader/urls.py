# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('upload-success/', views.upload_file, name='upload_success'),  # Success page URL
]
