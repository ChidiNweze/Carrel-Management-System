from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE)
    gender_choices = [('M', 'Male'), ('F', 'Female'), ('X', 'Other')]
    first_name = models.CharField(max_length=200, null=True) #max length required for CharField
    last_name = models.CharField(max_length=200, null=True)
    student_ID = models.CharField(max_length=8, unique=True, null=True)
    Program = models.ForeignKey(
        'Program',
        null=True,
        default=None,
        on_delete=models.CASCADE)
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    floor = models.ForeignKey(
        'Floor',
        blank=True,
        on_delete=models.CASCADE,
        null=True)    
    Carrel = models.OneToOneField(
        'Carrel',
        blank=True,
        on_delete=models.CASCADE,
        null=True)
    carrel_allotted = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
    

    


class Carrel(models.Model):
    carrel_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy')]
    carrel_code = models.CharField(max_length=5)
    carrel_type = models.CharField(choices=carrel_choice, max_length=1, default=None)
    vacant = models.BooleanField(default=False)
    floor = models.ForeignKey('Floor', on_delete=models.CASCADE)

    def __str__(self):
        return self.carrel_code


class Floor(models.Model):
    level = models.IntegerField(unique=True)
    floor_choices = [('Q', 'Quiet Study'), ('S', 'Silent Study')]
    floor = models.CharField(
        choices=floor_choices,
        max_length=1,
        default=None,
        null=True)

    def __str__(self):
        return str(self.level)


class Program(models.Model):
    program = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.program

