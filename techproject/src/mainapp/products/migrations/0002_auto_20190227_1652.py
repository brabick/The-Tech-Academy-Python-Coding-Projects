# Generated by Django 2.0.7 on 2019-02-27 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('appetizers', 'appetizers'), ('treats', 'treats'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
