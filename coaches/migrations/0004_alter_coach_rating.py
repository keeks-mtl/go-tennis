# Generated by Django 3.2.3 on 2021-07-09 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_alter_coach_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
