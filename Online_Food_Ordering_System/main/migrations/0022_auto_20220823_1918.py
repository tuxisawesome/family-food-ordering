# Generated by Django 3.1.3 on 2022-08-23 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20220824_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='labels',
            field=models.CharField(blank=True, choices=[('School lunch', 'School lunch'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=25),
        ),
    ]
