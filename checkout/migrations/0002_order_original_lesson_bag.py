# Generated by Django 3.2.3 on 2021-07-09 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_lesson_bag',
            field=models.TextField(default=''),
        ),
    ]
