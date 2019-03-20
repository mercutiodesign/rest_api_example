from django.http import HttpResponse
from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-date')

def post(_request, post_id):
    return HttpResponse("post %d" % post_id)
