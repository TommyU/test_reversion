from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.CharField(max_length=32)
    status_list=(('draft','draft'),('pending','pending'),('published','published'))
    status = models.CharField(max_length=16, choices=status_list)
    create_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField()