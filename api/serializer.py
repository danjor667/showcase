from rest_framework.serializers import ModelSerializer
from projects.models import Project, Category, Comment, Vote
from users.models import Profile

class Projectserializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class Categoryserializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Commentserializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class Voteserializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class Profileserializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

