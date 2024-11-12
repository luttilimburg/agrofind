# Create your models here.
from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    filter_type = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.filter_type} - {self.image.name}"
