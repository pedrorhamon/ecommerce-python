from django.db import models


class Category(models.Model):

    name = models.CharField('Nome', max_length=100);
    slug = models.CharField('Identificador', max_length=100);

    create = models.CharField('Criado em', auto_now_add=True);
    modified = models.CharField('Identificador', auto_now=True);

class Meta:
    verbose_name = 'Categoria';
    verbose_name_plural = 'Categorias';
    ordering = ['name'];
    
class Product(models.Model):
    name = models.CharField('Nome', max_length=100);
    slug = models.CharField('Identificador', max_length=100);
    category = models.ForeignKey('catalog.Category', verbose_name='Categoria');
    description = models.TextField('Descrição', blank=True);
    price = models.DecimalField('Preço', decimal_places=2, max_digits=10);

    create = models.CharField('Criado em', auto_now_add=True);
    modified = models.CharField('Identificador', auto_now=True);




# Create your models here.
