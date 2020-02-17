# Generated by Django 2.0.5 on 2020-02-14 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('desig', models.CharField(max_length=50)),
                ('phonenum', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('verify_password', models.CharField(max_length=100)),
            ],
        ),
    ]
