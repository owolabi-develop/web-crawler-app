# Generated by Django 4.0.6 on 2022-09-24 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_products', '0003_movie_music_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='date_posted',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_posted',
            field=models.DateTimeField(),
        ),
    ]
