# Generated by Django 3.1.1 on 2020-09-28 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenshot',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='screenshot',
            name='screen_size',
        ),
        migrations.RemoveField(
            model_name='screenshot',
            name='title',
        ),
        migrations.AddField(
            model_name='screenshot',
            name='desktop_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='screenshot',
            name='mobile_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='screenshot',
            name='tablet_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
