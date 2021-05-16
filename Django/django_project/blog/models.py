from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from blog.base_model import BaseModel


# Create your models here.
class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # default value
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  # similarly to toString()
        return self.title
