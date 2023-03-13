from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin
)

from rest_framework import filters, viewsets

from client.models import Applicant
from .serializers import HomeHhSerializer, FollowSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class CreateRetrieveViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    pass


class Client(ReadOnlyModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = HomeHhSerializer


class PutchClient(RetrieveUpdateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = HomeHhSerializer
    permissions_classes = (IsOwnerOrReadOnly,)


class DelitClien(RetrieveDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = HomeHhSerializer
    permissions_classes = (IsOwnerOrReadOnly,)

class ImClient(ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = HomeHhSerializer
    permissions_classes = (IsOwnerOrReadOnly,)


class FollowViewSet(CreateRetrieveViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.follower.all()


#class Register()