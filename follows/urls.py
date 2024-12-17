from django.urls import path
from .views import FollowViewSet, FeedViewSet

urlpatterns = [
    path('follow/', FollowViewSet.as_view({'post': 'create'})),
    path('unfollow/<int:pk>/', FollowViewSet.as_view({'post': 'unfollow'})),
    path('feed/', FeedViewSet.as_view({'get': 'list'})),
]
