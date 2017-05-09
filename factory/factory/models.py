from django.db import models

# Create your models here.


class Factory(models.Model):
    name = models.CharField('Производитель', max_length= 250)
    product_link = models.ManyToManyField('Product')
    category_link = models.ManyToManyField('Category')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('Название продукта', max_length= 250)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('Название категории', max_length= 250)
    product_link = models.ManyToManyField('Product')

    def __str__(self):
        return self.name