# Generated by Django 2.0.7 on 2020-05-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('drinks', 'drinks'), ('appetizers', 'appetizers'), ('entrees', 'entrees')], max_length=60),
        ),
    ]
