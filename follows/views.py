from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Follow
from .serializers import FollowSerializer
from rest_framework.response import Response

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    @action(detail=False, methods=['post'])
    def create(self, request):
        # Implement follow logic here
        return Response("User Followed")

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        # Implement unfollow logic here
        return Response("User Unfollowed")

class FeedViewSet(viewsets.ViewSet):
    def list(self, request):
        # Implement feed logic here
        return Response("Feed Data")
