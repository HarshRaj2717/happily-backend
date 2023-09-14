from rest_framework.decorators import api_view
from rest_framework.response import Response

from authenticator.models import Users

from .models import Posts
from .serializers import PostsSerializer, PostsSerializerAll

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


@api_view(["GET"])
def get_specific_post(request, post_id):
    try:
        post = Posts.objects.get(id=post_id)
    except:
        return Response({
            'success': 0
        })
    post_serializer = PostsSerializerAll(post, many=False)
    return Response({
        'success': 1,
        'posts': post_serializer.data,
    })


@api_view(["POST"])
def create_post(request, user_key):
    data = request.data

    try:
        post = Posts.objects.create(
            created_by=Users.objects.get(api_token=user_key),
            title=data['title'].strip(),
            content=data['content'].strip()
        )
        post.save()
    except:
        return Response({'success': 0})

    return Response({'success': 1})


@api_view(["GET"])
def upvote_post(request, user_key, post_id):
    try:
        post = Posts.objects.get(id=post_id)
        vote_res = post.upvote(user_key)
    except:
        return Response({
            'success': 0,
        })

    return Response({
        'success': 1,
        'user_new_vote_value': vote_res['user_new_vote_value'],
        'post_total_votes': vote_res['post_total_votes'],
    })


@api_view(["GET"])
def downvote_post(request, user_key, post_id):
    try:
        post = Posts.objects.get(id=post_id)
        vote_res = post.downvote(user_key)
    except:
        return Response({
            'success': 0,
        })

    return Response({
        'success': 1,
        'user_new_vote_value': vote_res['user_new_vote_value'],
        'post_total_votes': vote_res['post_total_votes'],
    })
