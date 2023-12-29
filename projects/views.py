from rest_framework import status
from rest_framework import generics, mixins
from .serializer import Projectserializer
from .models import Project
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
################# function-based views ####################


@api_view(['GET', 'POST'])
def list_create(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = Projectserializer(projects, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = Projectserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete(request, pk):
    try:
        project = Project.objects.get(id=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Projectserializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = Projectserializer(project, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

# or use generic apiviews ################# generic apiviews ####################


class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = Projectserializer


generic_list_create = ProjectListCreate.as_view()


class ProjectDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = Projectserializer


generic_get_update_delete = ProjectDetailUpdateDelete.as_view()

############# class-based views ######################

class ListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = Projectserializer
    queryset = Project.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class_list_create = ListCreate.as_view()


class RetrieveUpdateDelete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = Projectserializer
    queryset = Project.objects.all()
    def get(self, request, *args, **kwargs):
        pk =kwargs.get("pk")
        if pk is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return self.retrieve(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

class_retrieve_update_delete = RetrieveUpdateDelete.as_view()