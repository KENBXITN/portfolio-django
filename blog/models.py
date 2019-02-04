from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40)
    publication_time = models.DateTimeField()
    body = models.TextField()
    top_image = models.ImageField(upload_to='images/')
