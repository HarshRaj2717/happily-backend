from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Posts
from .serializers import PostsSerializer

# Create your views here.


@api_view(["GET"])
def get_posts(request):
    posts = Posts.objects.all()
    posts_serializer = PostsSerializer(posts, many=True)
    print(posts_serializer)
    return Response({
        'success': 1,
        'posts': posts_serializer.data,
    })


@api_view(["POST"])
def create_post(request):
    ...
