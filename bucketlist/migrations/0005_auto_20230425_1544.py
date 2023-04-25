# Generated by Django 3.2.18 on 2023-04-25 15:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bucketlist', '0004_alter_list_planning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterUniqueTogether(
            name='list',
            unique_together={('user_name', 'title')},
        ),
    ]
