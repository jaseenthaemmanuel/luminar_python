# Generated by Django 2.0.5 on 2020-02-14 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempinher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='desig',
            field=models.CharField(max_length=100),
        ),
    ]
