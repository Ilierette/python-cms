# Generated by Django 4.2.1 on 2023-05-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_alter_banner_button_alter_banner_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='button',
        ),
        migrations.AddField(
            model_name='banner',
            name='button_CTA',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
