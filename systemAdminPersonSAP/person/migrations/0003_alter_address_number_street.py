# Generated by Django 4.0.3 on 2022-04-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_address_person_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='number_street',
            field=models.IntegerField(),
        ),
    ]