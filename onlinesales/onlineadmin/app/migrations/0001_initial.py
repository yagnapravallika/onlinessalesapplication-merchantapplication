# Generated by Django 2.2.2 on 2019-11-08 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Merchentlogin',
            fields=[
                ('merchentid', models.AutoField(primary_key=True, serialize=False)),
                ('merchentname', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('emailid', models.EmailField(max_length=254, unique=True)),
                ('contactno', models.IntegerField(unique=True)),
            ],
        ),
    ]
