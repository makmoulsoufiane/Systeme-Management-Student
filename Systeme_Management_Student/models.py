from django.db import models

class Group(models.Model):
    # Auto-incrementing ID for each group, serves as the primary key
    id_group = models.AutoField(primary_key=True)

    # Date when the group was created
    year_of_creation = models.DateField()

  
