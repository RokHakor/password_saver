from django.db import models

# Create your models here.
class Password(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"For {self.name}, password is '{self.password}'"