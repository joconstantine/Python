from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    cat_image = models.ImageField(upload_to="photos/categories", blank=True)

    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse("products_by_category", args=[self.slug])

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
