# Generated by Django 5.0.6 on 2024-05-08 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Katgeoriya nomi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories/', verbose_name='Kategoriya Rasmi')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='store.category', verbose_name='Kategoriya')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Mahsulot nomi')),
                ('price', models.FloatField(verbose_name='Mahsulot narxi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Saytga chiqarilgan vaqti')),
                ('quantity', models.IntegerField(default=0, verbose_name='Ombordagi soni')),
                ('description', models.TextField(blank=True, default='Tez orada bu yerda malumot boladi', verbose_name='Mahsulot haqida malumot')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('size', models.IntegerField(default=30, verbose_name='mm dagi olchami')),
                ('color', models.CharField(default='Kumush', max_length=30, verbose_name='Rangi/Materiyali')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category', verbose_name='Kategoriya')),
            ],
            options={
                'verbose_name': 'Mahsulot',
                'verbose_name_plural': 'Mahsulotlar',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Rasm')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.product')),
            ],
            options={
                'verbose_name': 'Rasm',
                'verbose_name_plural': 'Mahsulot Gallery',
            },
        ),
    ]
