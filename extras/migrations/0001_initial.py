# Generated by Django 3.2.13 on 2023-03-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('name', models.CharField(max_length=55)),
                ('subject', models.CharField(max_length=55)),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='HeroPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(blank=True, max_length=55, null=True)),
                ('user_content', models.PositiveIntegerField(choices=[(1, 'Left'), (2, 'Right')])),
                ('image_sub_title', models.CharField(blank=True, max_length=55, null=True)),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Hero Image Description')),
                ('image', models.ImageField(default='default.jpeg', upload_to='hero')),
                ('is_displayed', models.BooleanField(default=True)),
            ],
        ),
    ]
