from django.db import models

# Create your models here.
class student_data(models.Model):
    First_name = models.CharField(max_length = 10)
    Last_name = models.CharField(max_length = 10)
    current_class = models.IntegerField()
    roll_number = models.IntegerField()
    skills = models.CharField(max_length = 100)
    active = models.BooleanField(default = True)
