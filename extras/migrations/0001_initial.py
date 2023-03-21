# Generated by Django 3.2.13 on 2023-03-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=55)),
                ('image_sub_title', models.CharField(max_length=55)),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Hero Image Description')),
                ('image', models.ImageField(default='default.jpeg', upload_to='hero')),
                ('is_displayed', models.BooleanField(default=True)),
            ],
        ),
    ]
