# Generated by Django 4.2.1 on 2023-05-13 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_image', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
    ]
