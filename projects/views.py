from django.shortcuts import render
from users.models import Profile

# Create your views here.

def home(request):
    return render(request, 'home.html')

def home_detail(request, pk):
    profile = Profile.objects.get(id=pk)
    projects = profile.projects
    context = {"projects": projects}
    return render(request, 'home_detail.html', context)

