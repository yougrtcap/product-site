from django.contrib.auth.models import User
from django.db import models


# Categoryモデルを作成
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=150)
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Nice(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, primary_key=True)
    number = models.IntegerField(default=0)

    def increment(self):
        self.number += 1
        self.save()
