# Generated by Django 3.0.7 on 2023-04-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0008_alter_itinerary_id_alter_package_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='package',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
