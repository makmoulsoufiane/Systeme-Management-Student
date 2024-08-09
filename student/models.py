from django.db import models

# Create your models here.
class Student (models.Model):

    id_student = models.AutoField(primary_key=True)
    fullname_student = models.CharField(max_length=20)
    address_student = models.CharField(max_length=255)
    date_of_inscription_of_student = models.DateField()

    def __str__(self):
        return self.fullname_student