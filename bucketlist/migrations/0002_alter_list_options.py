# Generated by Django 3.2.18 on 2023-04-08 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['created_on']},
        ),
    ]
