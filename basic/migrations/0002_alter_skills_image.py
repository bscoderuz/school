# Generated by Django 4.1.5 on 2023-02-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='image',
            field=models.ImageField(upload_to='skills_pic'),
        ),
    ]
