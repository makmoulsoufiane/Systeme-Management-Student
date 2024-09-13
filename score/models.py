from django.db import models

# Create your models here.
class Score(models.Model):
    note=models.IntegerField()
    id_student=models.IntegerField()
    