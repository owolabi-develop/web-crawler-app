# Generated by Django 4.0.6 on 2022-09-28 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_products', '0020_alter_jobs_date_posted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobs',
            options={},
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='date_posted',
        ),
    ]
