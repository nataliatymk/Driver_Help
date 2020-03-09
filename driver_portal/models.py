from django.db import models

class Advice (models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=246)
    text = models.TextField()
    tags = models.CharField(max_length=128)

    def __str__(self):
        return self.title