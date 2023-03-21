# Generated by Django 4.1.7 on 2023-03-20 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.URLField(max_length=2000)),
                ('title', models.CharField(default=None, max_length=50)),
                ('text', models.CharField(max_length=255)),
                ('link', models.URLField(max_length=1000)),
            ],
        ),
    ]
