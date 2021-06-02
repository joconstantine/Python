from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
