# Generated by Django 3.2.13 on 2023-03-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='background_color',
            field=models.CharField(default='#FF2020', max_length=10),
        ),
    ]