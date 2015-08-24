from django.db import models
from django.contrib import admin
# Create your models here.
class IntroductionPage(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    time=models.DateTimeField()

class IntroductionPageAdmin(admin.ModelAdmin):
    list_display=('title','time')
admin.site.register(IntroductionPage,IntroductionPageAdmin)
