# Generated by Django 3.1 on 2023-02-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='tours/')),
                ('availability', models.BooleanField(default=True)),
                ('destination', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
