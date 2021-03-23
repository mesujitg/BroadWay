from django.db import models


class About(models.Model):
    title = models.CharField(max_length=256)
    details = models.TextField()
    image = models.ImageField(upload_to='about')

    def __str__(self):
        return self.title

