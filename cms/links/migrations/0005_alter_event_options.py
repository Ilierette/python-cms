# Generated by Django 4.2.1 on 2023-05-26 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0004_rename_socialmedia_socialmedialink'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Events', 'verbose_name_plural': 'Events'},
        ),
    ]
