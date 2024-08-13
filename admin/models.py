from django.db import models

# Create your models here.

class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True) 
    fullname_admin = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    date_of_inscription = models.DateField()
    
    
    def __str__(self):
        return self.fullname_admin


