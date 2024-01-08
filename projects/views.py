from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework import generics, mixins, authentication, permissions
from .serializer import ProjectSerializer
from .models import Project
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes


# Create your views here.
################# function-based views ####################


@api_view(['GET'])
@authentication_classes([authentication.SessionAuthentication, authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def list(request, *args, **kwargs):
    pk = kwargs.get('pk')
    if pk:
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([authentication.SessionAuthentication, authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def post(request, *args, **kwargs):
    user = request.user
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save(commit=False)
        instance.owner = user
        instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([authentication.SessionAuthentication, authentication.TokenAuthentication])
@permission_classes([permissions.IsAdminUser, IsOwnerOrReadOnly])
def update_delete(request, *args, **kwargs):
    pk = kwargs.get("pk")
    if pk:
        project = get_object_or_404(Project, pk=pk)
    if request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

#################### or use class-base apiviews #####################################


class ProjectList(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  generics.GenericAPIView):
    authentication_classes([authentication.SessionAuthentication, authentication.TokenAuthentication])
    permission_classes([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)


generic_list = ProjectList.as_view()


class ProjectCreate(generics.ListCreateAPIView):
    authentication_classes([authentication.SessionAuthentication, authentication.TokenAuthentication])
    permission_classes([permissions.IsAuthenticated])
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


generic_create = ProjectCreate.as_view()


class ProjectUpdateDelete(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    authentication_classes = ([authentication.SessionAuthentication, authentication.TokenAuthentication])
    permission_classes = ([permissions.IsAdminUser, IsOwnerOrReadOnly])
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


generic_update_delete = ProjectUpdateDelete.as_view()
