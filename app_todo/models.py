from django.db import models

# Create your models here.


class mission(models.Model):
    title = models.CharField(max_length=20)
    index = models.CharField(max_length=255)
    time = models.IntegerField(default=5)
    is_done = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)
    remained_days = models.IntegerField(default=5)
    username = models.CharField(max_length=20 , default="not-edited")

    def __str__(self):
        return self.title
    