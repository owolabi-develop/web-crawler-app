# Generated by Django 4.0.6 on 2022-09-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='newprice',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='oldPrice',
            field=models.IntegerField(),
        ),
    ]
