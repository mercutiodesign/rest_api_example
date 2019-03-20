from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def index(request):
    return render(request, 'news/index.html', {'posts': Post.objects.all()})


def post(_request, post_id):
    return HttpResponse("post %d" % post_id)
