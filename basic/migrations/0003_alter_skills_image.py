# Generated by Django 4.1.5 on 2023-02-07 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_alter_skills_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='image',
            field=models.ImageField(upload_to='media/skills_pic'),
        ),
    ]
