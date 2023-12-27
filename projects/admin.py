from django.contrib import admin
from .models import Project, Comment, Category, Vote

# Register your models here.
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Vote)