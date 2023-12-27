from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import Projectserializer
from projects.models import Project


@api_view(['GET'])
def endpoints(request):
    return Response({})


@api_view(['GET', 'POST'])
def projects(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = Projectserializer(projects, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = Projectserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def update_delete(request, pk):
    try:
        project = Project.objects.get(id=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Projectserializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = Projectserializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


