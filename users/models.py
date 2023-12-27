from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField()
    email = models.EmailField()
    bio = models.TextField(max_length=1000, null=True, blank=True)
    school = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    github = models.URLField(null=True, blank=True)
    LinkedIn = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resume = models.FileField(null=True, blank=True)



    def __str__(self):
        return self.user.username


    @property
    def projects(self):
        return self.project_set.all()

