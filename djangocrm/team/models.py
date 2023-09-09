from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'user'

    def __str__(self) -> str:
        return self.first_name
