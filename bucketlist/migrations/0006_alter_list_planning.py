# Generated by Django 3.2.18 on 2023-05-10 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlist', '0005_auto_20230425_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='planning',
            field=models.TextField(default='Add plan here'),
        ),
    ]
