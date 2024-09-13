# Group/models.py
from django.db import models

class Group(models.Model):
    id_group = models.AutoField(primary_key=True)
    year_of_creation = models.PositiveIntegerField()

    def __str__(self):
        return f"Group {self.id_group} - {self.year_of_creation}"
