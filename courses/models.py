from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    details = models.TextField()
    fee = models.FloatField()
    image = models.ImageField(upload_to='courses', null=True, blank=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ('name', 'duration', 'fee', 'details')

