from django.urls import path, include
from django.utils import timezone
from rest_framework import routers, serializers, viewsets

from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ('date',)

    def to_internal_value(self, data: dict):
        result = super().to_internal_value(data)
        result['date'] = timezone.now()
        return result


# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

api_urls = [
    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
