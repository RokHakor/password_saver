from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Password_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"For {self.name}, password is '{self.password}'"