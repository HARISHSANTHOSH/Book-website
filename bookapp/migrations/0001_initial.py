# Generated by Django 4.1.7 on 2023-02-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shopregistermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('shopid', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
