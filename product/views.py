"""
API for Product

"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

from .models import Product, Categories, ProductCategories, Color, ProductColor, ApparelSize, ProductHasColors
from .productcontroller import ProductController

from .serializers import ProductSerializer, CategoriesSerializer, ProductCategoriesSerializer,ColorSerializer, ProductColorSerializer, ApparelSizeSerializer, ProductHasColorsSerializer


# Product Controller
product_controller = ProductController()

class ProductViewset(viewsets.ModelViewSet):
    """ Pruduct CRUD"""
    queryset=Product.objects.all()
    serializer_class= ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        """CREATE a Product"""

        result = product_controller.create_product(request.data)
        return result

    def update(self, request, *args, **kwargs):
        """Update an Existing Product"""

        result = product_controller.update_product(request.data)
        return result

    def list(self, request, *args, **kwargs):
        """Get list of product"""
        result = product_controller.get_product(request.data)
        return result

    def delete(self, request, product_id):
        """ Delete product"""
        result = product_controller.delete_product(product_id)
        return result

class CategoriesViewset(viewsets.ModelViewSet):
    """  Categories CRUD """
    queryset=Categories.objects.all()
    serializer_class=CategoriesSerializer
    permission_classes=[AllowAny,]

    def create(self, request, *args, **kwargs):
        """CREATE a Categories"""

        result = product_controller.create_category(request.data)
        return result

    def update(self, request, *args, **kwargs):
        """Update an Existing Catergory"""

        result = product_controller.update_category(request.data)
        return result

    def list(self, request, *args, **kwargs):
        """Get list of product"""
        result = product_controller.get_category(request.data)
        return result

    def delete(self, request, category_id):
        """ Delete product"""
        result = product_controller.delete_category(category_id)
        return result


class ProductCategoriesViewset(viewsets.ModelViewSet):
    """ CRUD"""
    queryset=ProductCategories.objects.all()
    serializer_class=ProductCategoriesSerializer
    permission_classes=[AllowAny,]

    def create(self, request, *args, **kwargs):
        """CREATE a Categories"""

        result = product_controller.create_productcategory(request.data)
        return result

    def list(self, request, *args, **kwargs):
        """Get list of product"""
        result = product_controller.get_productcategory(request.data)
        return result

    def delete(self, request, productcategories_id):
        """ Delete product"""
        result = product_controller.delete_productcategory(productcategories_id)
        return result

class ColorViewset(viewsets.ModelViewSet):
    """ CRUD"""
    queryset=Color.objects.all()
    serializer_class=ColorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        """CREATE a Color"""

        result = product_controller.create_color(request.data)
        return result

    def update(self, request, *args, **kwargs):
        """Update an Existing Color"""

        result = product_controller.update_color(request.data)
        return result

    def list(self, request, *args, **kwargs):
        """Get list of color"""
        result = product_controller.get_color(request.data)
        return result

    def delete(self, request, color_id):
        """ Delete color"""
        result = product_controller.delete_color(color_id)
        return result

class ProductColorViewset(viewsets.ModelViewSet):
    """ CRUD"""
    queryset=ProductColor.objects.all()
    serializer_class=ProductColorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        """CREATE a Color"""

        result = product_controller.create_productcolor(request.data)
        return result

    def list(self, request, *args, **kwargs):
        """Get list of color"""
        result = product_controller.get_productcolor(request.data)
        return result

    def delete(self, request, productcolor_id):
        """ Delete color"""
        result = product_controller.delete_productcolor(productcolor_id)
        return result


class ApparelSizeViewset(viewsets.ModelViewSet):
    """ CRUD"""
    queryset=ApparelSize.objects.all()
    serializer_class=ApparelSizeSerializer
    permission_classes=[AllowAny,]

    def create(self, request, *args, **kwargs):
        """CREATE a Color"""

        result = product_controller.create_apparelsize(request.data)
        return result

    def update(self, request, *args, **kwargs):
        """Update an Existing Color"""

        result = product_controller.update_apperalsize(request.data)
        return result

    def list(self, request, *args, **kwargs):
        """Get list of color"""
        result = product_controller.get_apperalsize(request.data)
        return result

    def delete(self, request, apperalsize_id):
        """ Delete color"""
        result = product_controller.delete_apperalsize(apperalsize_id)
        return result


class ProductHasColorViewset(viewsets.ModelViewSet):
    """ CRUD"""
    queryset=ProductHasColors.objects.all()
    serializer_class=ProductHasColorsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        """CREATE a ProductHasColor"""

        result = product_controller.create_producthascolor(request.data)
        return result

    def list(self, request, *args, **kwargs):
        """Get list of color"""
        result = product_controller.get_producthascolor(request.data)
        return result

    def delete(self, request, producthascolor_id):
        """ Delete color"""
        result = product_controller.delete_producthascolor(producthascolor_id)
        return result



