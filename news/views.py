from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Post


class PostList(generic.ListView):
    model = Post


class PostCreate(generic.CreateView):
    model = Post
    fields = ['title', 'text']
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.date = timezone.now()
        return super().form_valid(form)


class PostDetail(generic.DetailView):
    model = Post
    fields = "__all__"


class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index")
