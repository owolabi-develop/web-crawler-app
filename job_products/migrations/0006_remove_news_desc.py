# Generated by Django 4.0.6 on 2022-09-25 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_products', '0005_alter_news_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='desc',
        ),
    ]
