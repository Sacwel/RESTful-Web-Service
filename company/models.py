from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_number = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.name
