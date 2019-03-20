from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('new-post/', views.PostCreate.as_view(), name='new-post'),
    path('delete-post/<int:pk>', views.PostDelete.as_view(), name='delete-post'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post'),
]
