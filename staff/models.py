from django.db import models
from django.contrib.auth.models import AbstractUser


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=50)
    sections = models.ManyToManyField(Section)

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
