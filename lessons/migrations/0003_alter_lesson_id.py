# Generated by Django 3.2.3 on 2021-06-03 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20210603_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]