from django.db import models


# Create your models here.
class Ariticle(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return "<Ariticle: %s>" % self.title
