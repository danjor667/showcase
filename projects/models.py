
from django.db import models
from django.contrib.auth.models import User



class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="project/photo/")
    demo_video = models.FileField(upload_to="project/demo_video/")
    source_code_link = models.URLField()
    link = models.URLField()
    category = models.ManyToManyField('Category')
    new_category = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.name

    def delete(self):
        self.image.delete()
        self.demo_video.delete()
        super().delete()

    @property
    def comments(self):
        return self.comment_set.all()


    @property
    def votes(self):
        return self.vote_set.all()


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    body = models.TextField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:30]


class Vote(models.Model):
    up_vote = "up vote"
    down_vote = "down vote"
    options = {up_vote: "UP VOTE",
               down_vote: "DOWN VOTE"}
    projects = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False)
    vote = models.CharField(max_length=50, choices=options, default=up_vote)
