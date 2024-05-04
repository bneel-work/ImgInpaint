from django.db import models

# Create your models here.

class ImgInpaintModel(models.Model):
    name = models.CharField(max_length=100)
    damaged_img = models.ImageField(upload_to='static/img/damaged_img')
    masked_img = models.ImageField(upload_to='static/img/masked_img')
    result_img = models.ImageField(upload_to='static/img/result_img', blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

