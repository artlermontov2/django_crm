from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.EmailField(max_length=256) 
    description = models.TextField()
    worker = models.CharField(max_length=128)
    data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Клиент {self.name}'
    
    
    

