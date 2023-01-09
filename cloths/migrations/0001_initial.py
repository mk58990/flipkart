# Generated by Django 4.1.5 on 2023-01-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=10)),
                ('dop', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('quantity', models.IntegerField()),
                ('gender', models.BooleanField()),
            ],
        ),
    ]