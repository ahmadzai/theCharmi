from django.db import models
from django.conf import settings
from blog.models import BlogPost


class HomeContent(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    hero_image = models.ImageField(upload_to='hero_images/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Slider(models.Model):
    small_title = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    text = models.TextField()
    slider_image = models.ImageField(upload_to='slider_images/', blank=True, null=True)
    button_link = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, null=True, blank=True, related_name='sliders')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
