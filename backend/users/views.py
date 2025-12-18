from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Follow
from posts.models import Post
from posts.serializers import PostSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, id):
    try:
        user_to_follow = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    if user_to_follow == request.user:
        return Response({"error": "You cannot follow yourself"}, status=400)

    Follow.objects.get_or_create(
        follower=request.user,
        following=user_to_follow
    )
    return Response({"message": "User followed successfully"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):
    following_ids = Follow.objects.filter(
        follower=request.user
    ).values_list('following', flat=True)

    posts = Post.objects.filter(user__id__in=following_ids).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
