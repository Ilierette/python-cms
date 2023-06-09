# Generated by Django 4.2.1 on 2023-05-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('pub_date', models.DateTimeField(null=True, verbose_name='date published')),
                ('event_date', models.DateTimeField(null=True, verbose_name='event date')),
                ('description', models.TextField(max_length=1000, null=True)),
                ('url', models.URLField(null=True)),
            ],
        ),
    ]
