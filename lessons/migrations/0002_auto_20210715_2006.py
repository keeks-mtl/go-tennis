# Generated by Django 3.2.3 on 2021-07-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='students',
        ),
        migrations.AlterField(
            model_name='classtype',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='classtype',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
