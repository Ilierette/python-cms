# Generated by Django 4.2.1 on 2023-05-27 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_alter_banner_button_alter_menuitem_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='button',
            field=models.SlugField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(null=True, upload_to='banners'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.menuitem'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.SlugField(blank=True, default='', max_length=200, null=True),
        ),
    ]
