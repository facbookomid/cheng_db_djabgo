from django.db import models


class Student(models.Model):
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return f'{self.name}{self.last_name}'
