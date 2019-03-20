from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:post_id>', views.post, name='post'),
]