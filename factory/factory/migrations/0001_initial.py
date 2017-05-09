# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Производитель')),
                ('category_link', models.ManyToManyField(to='factory.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название продукта')),
            ],
        ),
        migrations.AddField(
            model_name='factory',
            name='product_link',
            field=models.ManyToManyField(to='factory.Product'),
        ),
        migrations.AddField(
            model_name='category',
            name='product_link',
            field=models.ManyToManyField(to='factory.Product'),
        ),
    ]