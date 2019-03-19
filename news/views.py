from django.shortcuts import render
from django.http import HttpResponse


def index(_request):
    return HttpResponse("Hello, world. You're at the news index.")