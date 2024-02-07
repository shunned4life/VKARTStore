from django.db import models


class Employee(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username + " " + self.password
