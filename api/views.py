from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view



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