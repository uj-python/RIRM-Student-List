# Generated by Django 3.2.8 on 2021-10-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20211019_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentslist',
            name='Id',
        ),
        migrations.AddField(
            model_name='studentslist',
            name='id',
            field=models.CharField(default='1', max_length=10, primary_key=True, serialize=False),
        ),
    ]