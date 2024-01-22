from rest_framework.serializers import ModelSerializer
from projects.models import Project, Category, Comment, Vote

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {"owner": {"read_only": True},
                        "new_category": {"write_only": True}}


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {"owner": {"read_only": True}}


class Voteserializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


