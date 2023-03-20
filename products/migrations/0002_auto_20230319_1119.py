# Generated by Django 3.2.13 on 2023-03-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Category Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Category Slug')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Category Description')),
                ('image', models.ImageField(default='default.jpeg', upload_to='category')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Product Description'),
        ),
        migrations.AddField(
            model_name='products',
            name='is_liked',
            field=models.BooleanField(default=False, verbose_name='You may Like'),
        ),
        migrations.AddField(
            model_name='products',
            name='is_trending',
            field=models.BooleanField(default=False, verbose_name='Trending'),
        ),
        migrations.AlterField(
            model_name='products',
            name='discounted_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Discounted price'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Product Price'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=50, verbose_name='Product Name'),
        ),
    ]