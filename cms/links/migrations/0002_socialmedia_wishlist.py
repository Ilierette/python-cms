# Generated by Django 4.2.1 on 2023-05-26 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Social Media',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(max_length=1000, null=True)),
            ],
        ),
    ]