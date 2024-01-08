from .models import User, Profile
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework import permissions, authentication
from .permissions import IsMe
from rest_framework import generics, mixins
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.response import Response



# Create your views here.
## list users view


@api_view(['GET'])
@authentication_classes([authentication.SessionAuthentication, authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def list(request, *args, **kwargs):
    pk = kwargs.get('pk')
    if pk:
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request, *args, **kwargs):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
@authentication_classes([authentication.SessionAuthentication, authentication.TokenAuthentication])
@permission_classes([permissions.IsAdminUser, IsMe])
def update_delete(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user = get_object_or_404(User, pk=pk)
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        serializer.save()
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_200_OK)

########### generic api views ############

class UserList(mixins.ListModelMixin, mixins.RetrieveModelMixin,generics.GenericAPIView):
    pass
# todo implemente this view

class UserCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

generic_create = UserCreate.as_view()


class UserUpdateDelete(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    authentication_classes = ([authentication.SessionAuthentication, authentication.TokenAuthentication])
    permission_classes = ([IsMe])
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def put(self, request, *args, **kwargs):
        print(request.user)
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        print(request.user)
        return self.destroy(request, *args,**kwargs)

generic_update_delete = UserUpdateDelete.as_view()


################### profile related views ################
# todo implement the views related to Profile CRUD operations

