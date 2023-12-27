from rest_framework.serializers import ModelSerializer
from projects.models import Project, Category, Comment, Vote
from users.models import Profile

class Projectserializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


