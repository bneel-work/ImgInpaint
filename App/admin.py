from django.contrib import admin
from .models import ImgInpaintModel
# Register your models here.


class ImgInpaintAdmin(admin.ModelAdmin):
    list_display = ['name', 'dateCreated', 'dateUpdated']


admin.site.register(ImgInpaintModel, ImgInpaintAdmin)