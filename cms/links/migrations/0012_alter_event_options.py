# Generated by Django 4.2.1 on 2023-05-27 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0011_alter_affiliatelink_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event_date'], 'verbose_name': 'Events', 'verbose_name_plural': 'Events'},
        ),
    ]
