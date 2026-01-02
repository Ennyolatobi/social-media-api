from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, FeedView, LikePostView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", FeedView.as_view(), name="feed"),
    path("like/<int:post_id>/", LikePostView.as_view(), name="like-post"),
]
