"""
Serializers of Product App
"""

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product, Categories, ProductCategories, Color, ProductColor, ApparelSize, ProductHasColors

class ProductSerializer(ModelSerializer):

   """Serializes all fields of the Product model"""
   product_id = SerializerMethodField()

   def get_product_id(self, obj):
        if obj.id:
            return obj.id

   class Meta:
       model = Product
       fields = ['product_id', 'name', 'description','price', 'stock']


class CategoriesSerializer(ModelSerializer):
    """ Serializes all fields of the Categories Model"""
    category_id = SerializerMethodField()
    def get_category_id(self, obj):
        if obj.id:
            return obj.id

    class Meta:
        model = Categories
        fields = ['category_id','name','description']

class ProductCategoriesSerializer(ModelSerializer):

    product_name = SerializerMethodField('get_product_name', allow_null=True, required=False)
    def get_product_name(self,obj):
        return obj.product.name

    category_name = SerializerMethodField('get_category_name', allow_null=True, required=False)
    def get_category_name(self, obj):
        return obj.category.name

    category_discription = SerializerMethodField('get_category_discription', allow_null=True, required=False)
    def get_category_discription(self, obj):
        return obj.category.description

    productcategories_id = SerializerMethodField()
    def get_productcategories_id(self, obj):
        if obj.id:
            return obj.id
    class Meta:
        model = ProductCategories
        fields = ['productcategories_id','name', 'ptype', 'category','category_name','category_discription','product','product_name']

class ColorSerializer(ModelSerializer):
    """ Serializes all fields of the Color Model"""
    color_id = SerializerMethodField()
    def get_color_id(self, obj):
        if obj.id:
            return obj.id
    class Meta:
        model = Color
        fields = ['color_id','name','code','product_color']

class ProductColorSerializer(ModelSerializer):
    """ Serializes all fields of the ProductColor Model"""
    productcolor_id = SerializerMethodField()
    def get_productcolor_id(self, obj):
        if obj.id:
            return obj.id
    class Meta:
        model = ProductColor
        fields = ['productcolor_id','name']

class ApparelSizeSerializer(ModelSerializer):
    apperalsize_id = SerializerMethodField()
    def get_apperalsize_id(self, obj):
        if obj.id:
            return obj.id
    class Meta:
        model = ApparelSize
        fields = ['apperalsize_id','name','size','code','order_no','product']

class ProductHasColorsSerializer(ModelSerializer):

    product = SerializerMethodField('get_product_name')
    def get_product_name(self,obj):
        return obj.product.name

    product_color = SerializerMethodField('get_productcolor_name')
    def get_productcolor_name(self,obj):
        return obj.product_color.name

    producthascolor_id= SerializerMethodField()
    def get_producthascolor_id(self, obj):
        if obj.id:
            return obj.id
    class Meta:
        model = ProductHasColors
        fields = ['producthascolor_id','product','product_color','description']