# Generated by Django 4.1.7 on 2023-03-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0008_alter_bookmodel_bookpdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='bookdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]