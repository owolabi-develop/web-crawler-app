# Generated by Django 4.0.6 on 2022-09-26 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_products', '0011_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='desc',
            new_name='Price',
        ),
        migrations.AlterField(
            model_name='jobs',
            name='url',
            field=models.URLField(max_length=255),
        ),
    ]
