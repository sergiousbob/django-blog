# Generated by Django 4.2 on 2023-05-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Подробнее', max_length=255),
        ),
    ]
