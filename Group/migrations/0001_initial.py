# Generated by Django 5.1 on 2024-08-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id_group', models.AutoField(primary_key=True, serialize=False)),
                ('year_of_creation', models.PositiveIntegerField()),
            ],
        ),
    ]
