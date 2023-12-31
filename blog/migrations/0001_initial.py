# Generated by Django 3.1 on 2023-02-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='blog/images/')),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
