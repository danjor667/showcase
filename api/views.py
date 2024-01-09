from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import obtain_auth_token



@api_view(['GET'])
def endpoints(request):
    routes = [
        {'GET': '/api/projects/'},
        {'POST': '/api/projects/create/'},
        {'GET': '/api/projects/id/'},
        {'PUT': '/api/projects/id/update/'},
        {'DELETE': '/api/projects/id/delete/'}
    ]
    return Response(routes)
