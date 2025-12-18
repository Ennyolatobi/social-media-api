from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet
from users.views import follow_user, feed
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login/', TokenObtainPairView.as_view()),
    path('api/', include(router.urls)),
    path('api/follow/<int:id>/', follow_user),
    path('api/feed/', feed),
]
