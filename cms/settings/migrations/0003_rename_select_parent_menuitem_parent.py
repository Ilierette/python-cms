# Generated by Django 4.2.1 on 2023-05-27 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_rename_banners_banner_alter_banner_options_menuitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='select_parent',
            new_name='parent',
        ),
    ]
