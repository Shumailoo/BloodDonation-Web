# Generated by Django 4.1.4 on 2022-12-28 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_alter_staff_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical_information',
            name='last_donation',
            field=models.DateField(blank=True, null=True),
        ),
    ]
