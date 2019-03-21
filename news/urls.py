from django.urls import path
from django.views.generic import RedirectView

from . import views
from .rest_api import api_urls

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('favicon.ico', RedirectView.as_view(url='/static/news/favicon.ico', permanent=True)),
    path('new-post', views.PostCreate.as_view(), name='new-post'),
    path('delete-post/<int:pk>', views.PostDelete.as_view(), name='delete-post'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post'),
] + api_urls
