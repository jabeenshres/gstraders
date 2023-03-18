# Generated by Django 4.1.7 on 2023-03-15 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(default='default.jpg', upload_to='trending')),
            ],
        ),
    ]
