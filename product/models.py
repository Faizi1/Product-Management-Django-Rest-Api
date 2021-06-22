"""
Model for Product app
"""

from django.db import models



class Categories(models.Model):
    """ Category Model """
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProductColor(models.Model):
    """ Product Color """
    name = models.CharField(max_length=10)

class Color(models.Model):
    """ Color Model """
    name = models.CharField(max_length=10)
    code = models.IntegerField()
    product_color = models.ForeignKey(ProductColor, on_delete=models.CASCADE,null=True)

class Product(models.Model):
    """ Product Model """
    name=models.CharField(max_length=15)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock=models.DecimalField(max_digits=9, decimal_places=0)

    def __str__(self):
        return self.name

class ProductCategories(models.Model):
    """ Product Categories """
    name = models.CharField(max_length=20)
    ptype = models.CharField(max_length=20)
    category=models.OneToOneField(Categories, on_delete=models.CASCADE,null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)

class ProductHasColors(models.Model):
    """ Product Colors """
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ProductHasColors_product_field')
    product_color= models.ForeignKey(ProductColor, on_delete=models.CASCADE, related_name='ProductColors_color_field')
    description=models.TextField()

class ApparelSize(models.Model):
    """ ApparelSize """
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    code = models.IntegerField()
    order_no = models.IntegerField()
    product =models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name