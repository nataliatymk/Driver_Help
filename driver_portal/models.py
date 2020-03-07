from django.db import models

class Advice (models.Model):
    title = models.CharField(max_length=246)
    date = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=32)

    def __str__(self):
        return self.title