# Generated by Django 3.2.18 on 2023-04-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelblog', '0004_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Where Next?', max_length=200),
        ),
    ]
