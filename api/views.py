from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import Projectserializer, Profileserializer
from projects.models import Project
from users.models import Profile


@api_view(['GET'])
def endpoints(request):
    routes = [
        {'GET': '/api/projects/'},
        {'GET': '/api/projects/id/'},
        {'POST': 'api/projects/create/'},
        {'PUT': '/api/projects/id/update/'},
        {'DELETE': '/api/projects/id/delete/'}
    ]
    return Response(routes)


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


@api_view(['GET', 'POST'])
def profiles(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = Profileserializer(profiles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Projectserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def profile_update(request, pk):
    try:
        profile = Profile.objects.get(id=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Profileserializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = Profileserializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_202_ACCEPTED)