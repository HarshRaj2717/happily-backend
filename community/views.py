from rest_framework.decorators import api_view
from rest_framework.response import Response

from authenticator.models import Users

from .models import Comments, Posts
from .serializers import CommentsSerializer, PostsSerializer

# Create your views here.


@api_view(["GET"])
def get_posts(request):
    posts = Posts.objects.all().order_by('-created_on')
    posts_serializer = PostsSerializer(posts, many=True)
    return Response({
        'success': 1,
        'posts': posts_serializer.data,
    })


@api_view(["GET"])
def get_comments(request, post_id):
    try:
        post = Posts.objects.get(id=post_id)
        comments = Comments.objects.filter(for_post=post).order_by('-created_on')
    except:
        return Response({
            'success': 0
        })
    comment_serializer = CommentsSerializer(comments, many=True)
    return Response({
        'success': 1,
        'posts': comment_serializer.data,
    })


@api_view(["POST"])
def add_comment(request, user_key, post_id):
    data = request.data
    try:
        assert data['content'].strip() != ""
        post = Posts.objects.get(id=post_id)
        post.add_comment(user_key, data['content'])
        return Response({"success": 1})
    except:
        return Response({"success": 0})


@api_view(["POST"])
def create_post(request, user_key):
    data = request.data

    try:
        assert data['title'].strip() != ""
        assert data['content'].strip() != ""
        post = Posts.objects.create(
            created_by=Users.objects.get(api_token=user_key),
            title=data['title'].strip(),
            content=data['content'].strip()
        )
        post.save()
        return Response({'success': 1})
    except:
        return Response({'success': 0})


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


@api_view(["DELETE"])
def delete_post(request, user_key, post_id):
    try:
        post = Posts.objects.get(id=post_id)
        assert Users.objects.get(api_token=user_key) == post.created_by
        post.delete()
        return Response({'success': 1})
    except:
        return Response({'success': 0})


@api_view(["DELETE"])
def delete_comment(request, user_key, post_id, comment_id):
    try:
        post = Posts.objects.get(id=post_id)
        post.delete_comment(user_key, comment_id)
        return Response({'success': 1})
    except:
        return Response({'success': 0})
