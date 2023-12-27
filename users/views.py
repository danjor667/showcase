from django.shortcuts import render
from .models import Profile

# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, 'users/profiles.html', context)


def profile_details(request, pk):
    profile = Profile.objects.get(id=pk)
    projects = profile.projects
    context = {"profile": profile, "projects": projects}
    return render(request, 'users/detail_profile.html', context)
