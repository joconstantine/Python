from django.db import models
from blog.base_model import BaseModel
from django.contrib.auth.models import User
from PIL import Image


class Profile(BaseModel):
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)  # if user is deleted, delete the profile (1-way)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # save first

        img = Image.open(self.image.path)  # open the image

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)  # overwrite the uploaded image
