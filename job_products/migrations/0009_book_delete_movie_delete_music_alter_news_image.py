# Generated by Django 4.0.6 on 2022-09-26 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_products', '0008_alter_news_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('image', models.URLField(max_length=255)),
            ],
            options={
                'ordering': ['Title'],
            },
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Music',
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.URLField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
