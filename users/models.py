from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.ForeignKey(
        "Section", on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default="default.img", upload_to='profile_pics')
    bio = models.CharField(max_length=2000, blank=True)
    skills = models.CharField(max_length=2000, blank=True)
    aoi = models.CharField(max_length=2000, blank=True)
    github = models.CharField(max_length=2000, blank=True)
    linkden = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
