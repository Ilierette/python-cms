# Generated by Django 4.2.1 on 2023-05-27 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Banners',
            new_name='Banner',
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Banner', 'verbose_name_plural': 'Banners'},
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('url', models.URLField(null=True)),
                ('select_parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.menuitem')),
            ],
        ),
    ]
