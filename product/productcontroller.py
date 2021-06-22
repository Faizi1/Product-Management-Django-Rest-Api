"""
Controller for the Product App

ProductController

"""

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from rest_framework.response import Response

from .models import Product, Categories, Color, ApparelSize, ProductCategories, ProductColor, ProductHasColors
from .serializers import (ProductSerializer,
            CategoriesSerializer,
            ColorSerializer,
            ApparelSizeSerializer,
            ProductCategoriesSerializer,
            ProductColorSerializer,
            ProductHasColorsSerializer)

class ProductController():
    """Business logic for the Product app"""

    def create_product(self, payload_data):
        """Create a product
        Returns:
            [dict]: [Message Object with keys: status, error,
                                    message and data]
        """
        try:
            serialized = ProductSerializer(data=payload_data)

            if serialized.is_valid(raise_exception=True):

                # Rollback db transaction if exception is thrown
                with transaction.atomic():

                    product = serialized.save()
                    serialized_product = ProductSerializer(product)

                return Response({'Error': False, 'Message':'Product Created!!','Status': 200,'data':serialized_product.data})
        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def update_product(self, payload_data):
        """Update a Product

        Args:
            payload_data ([dict]): [attribute (dict) of the request
                                    made by the client]
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """

        # product_id must exist
        product_id = payload_data.get('product_id')
        if not product_id:
            message = {
                "product_id": ["please provide product_id"]
            }
            return Response({'Error': True, 'Message':message,'Status': 500,'data':[]})

        # product_id must be an int
        try:
            product_id = int(product_id)
        except ValueError as err:
            message = {
                "product_id": ["product_id must be integer not string"]
            }
            return Response({'Error': True, 'Message':message,'Status': 500,'data':[]})

        try:
            product = Product.objects.get(pk=product_id)

            serialized = ProductSerializer(product, data=payload_data, partial =True)

            if serialized.is_valid():

                # Rollback db transaction if exception is thrown
                with transaction.atomic():
                    serialized.save()

                return Response({'Error': False, 'Message':'Product Updated!!','Status': 200,'data':serialized.data})

            return Response({'Error': True, 'Message':serialized.errors,'Status': 500,'data':[]})

        except ObjectDoesNotExist:
            return Response({'Error': True, 'Message':"Not Found",'Status': 500,'data':[]})

        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def get_product(self, request):
        """ Get list of Product
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            product = Product.objects.all()
            serializer =  ProductSerializer(product, many=True)
            return Response({'Error': False, 'Message':'Product Data','Status': 200,'data':serializer.data})
            # return Response({'Error': True, 'Message':serializer.errors,'Status': 500,'data':[]})

        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def delete_product(self, product_id):
        """Delete product
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            product = Product.objects.get(pk=product_id)
            product.delete()

            # Rollback db transaction if exception is thrown
            with transaction.atomic():
                product.save()
                serialized = ProductSerializer(product)
            return Response({'Error': False, 'Message':'Product Delete Successfully','Status': 200,'data':[]})

        except ObjectDoesNotExist:
            return Response({'Error': True, 'Message':"Not Found",'Status': 500,'data':[]})
        except Exception as e:
            return Response({'Error':True, 'Message':'Unsuccessfull','Status':500,'data':[str(e)]})




# Categories Busniess Logic

    def create_category(self, payload_data):
        """Create a category
        Returns:
            [dict]: [Message Object with keys: status, error,
                                    message and data]
        """
        try:
            serialized = CategoriesSerializer(data=payload_data)

            if serialized.is_valid(raise_exception=True):

                # Rollback db transaction if exception is thrown
                with transaction.atomic():

                    category = serialized.save()
                    serialized_category = CategoriesSerializer(category)

                return Response({'Error': False, 'Message':'category Created!!','Status': 200,'data':serialized_category.data})
        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def update_category(self, payload_data):
        """Update a category
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """

        # category_id must exist
        category_id = payload_data.get('category_id')
        if not category_id:
            message = {
                "category_id": ["please provide category_id"]
            }
            return Response({'Error': True, 'Message':message,'Status': 500,'data':[]})

        # category_id must be an int
        try:
            category_id = int(category_id)
        except ValueError as err:
            message = {
                "category_id": ["category_id must be integer not string"]
            }
            return Response({'Error': True, 'Message':message,'Status': 500,'data':[]})

        try:
            category = Categories.objects.get(pk=category_id)

            serialized = CategoriesSerializer(category, data=payload_data, partial=True)

            if serialized.is_valid():

                # Rollback db transaction if exception is thrown
                with transaction.atomic():
                    serialized.save()

                return Response({'Error': False, 'Message':'Category Updated!!','Status': 200,'data':serialized.data})

            return Response({'Error': True, 'Message':serialized.errors,'Status': 500,'data':[]})

        except ObjectDoesNotExist:
            return Response({'Error': True, 'Message':"Not Found",'Status': 500,'data':[]})

        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def get_category(self, request):
        """ Get list of Product
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            category = Categories.objects.all()
            serializer =  CategoriesSerializer(category, many=True)
            return Response({'Error': False, 'Message':'Category Data','Status': 200,'data':serializer.data})

        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def delete_category(self, category_id):
        """Delete category
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            category = Categories.objects.get(pk=category_id)
            category.delete()

            # Rollback db transaction if exception is thrown
            with transaction.atomic():
                category.save()
                serialized = CategoriesSerializer(category)
            return Response({'Error': False, 'Message':'Category Delete Successfully','Status': 200,'data':[]})

        except ObjectDoesNotExist:
            return Response({'Error': True, 'Message':"Not Found",'Status': 500,'data':[]})

# Busniess Logic of Color

    def create_color(self, payload_data):
        """Create a product
        Returns:
            [dict]: [Message Object with keys: status, error,
                                    message and data]
        """
        try:
            serialized = ColorSerializer(data=payload_data)

            if serialized.is_valid(raise_exception=True):

                # Rollback db transaction if exception is thrown
                with transaction.atomic():

                    color = serialized.save()
                    serialized_color = ColorSerializer(color)

                return Response({'Error': False, 'Message':'Color Created!!','Status': 200,'data':serialized_color.data})
        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def update_color(self, payload_data):
        """Update a color
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """

        # category_id must exist
        color_id = payload_data.get('color_id')
        if not color_id:
            message = {
                "color_id": ["please provide color_id"]
            }
            return Response({'Error': True, 'Message':message,'Status': 500,'data':[]})

        # category_id must be an int
        try:
            color_id = int(color_id)
        except ValueError as err:
            message = {
                "color_id": ["color_id must be integer not string"]
            }
            return Response({'Error': True, 'Message':message,'Status': 500,'data':[]})

        try:
            color = Color.objects.get(pk=color_id)

            serialized = ColorSerializer(color, data=payload_data, partial=True)

            if serialized.is_valid():

                # Rollback db transaction if exception is thrown
                with transaction.atomic():
                    serialized.save()

                return Response({'Error': False, 'Message':'Color Updated!!','Status': 200,'data':serialized.data})

            return Response({'Error': True, 'Message':serialized.errors,'Status': 500,'data':[]})

        except ObjectDoesNotExist:
            return Response({'Error': True, 'Message':"Not Found",'Status': 500,'data':[]})

        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def get_color(self, request):
        """ Get list of Color
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            color = Color.objects.all()
            serializer = ColorSerializer(color, many=True)
            return Response({'Error': False, 'Message':'Color Data','Status': 200,'data':serializer.data})

        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def delete_color(self, color_id):
        """Delete color
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            color = Color.objects.get(pk=color_id)
            color.delete()

            # Rollback db transaction if exception is thrown
            with transaction.atomic():
                color.save()
                serialized = ColorSerializer(color)
            return Response({'Error': False, 'Message':'Color Delete Successfully','Status': 200,'data':[]})
        except ObjectDoesNotExist:
            return Response({'Error': True, 'Message':"Not Found",'Status': 500,'data':[]})


# Busniess Logic of Apperalsize


    def create_apparelsize(self, payload_data):
        """Create a ApperalSize
        Returns:
            [dict]: [Message Object with keys: status, error,
                                    message and data]
        """
        try:
            serialized = ApparelSizeSerializer(data=payload_data)

            if serialized.is_valid(raise_exception=True):

                # Rollback db transaction if exception is thrown
                with transaction.atomic():

                    asize = serialized.save()
                    serialized_asize = ApparelSizeSerializer(asize)

                return Response({'Error': False, 'Message':'ApperalSize Created!!','Status': 200,'data':serialized_asize.data})
        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def update_apperalsize(self, payload_data):
        """Update a apperalsize
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """

        # apperalsize_id must exist
        apperalsize_id = payload_data.get('apperalsize_id')
        if not apperalsize_id:
            message = {
                "apperalsize_id": ["please provide apperalsize_id"]
            }
            return Response({'Error': True, 'Message':message,'Status': 500,'data':[]})

        # category_id must be an int
        try:
            apperalsize_id = int(apperalsize_id)
        except ValueError as err:
            message = {
                "apperalsize_id": ["apperalsize_id must be integer not string"]
            }
            return Response({'Error': True, 'Message':message,'Status': 500,'data':[]})

        try:
            asize = ApparelSize.objects.get(pk=apperalsize_id)

            serialized = ApparelSizeSerializer(asize, data=payload_data, parital = True)

            if serialized.is_valid():

                # Rollback db transaction if exception is thrown
                with transaction.atomic():
                    serialized.save()

                return Response({'Error': False, 'Message':'ApperalSize Updated!!','Status': 200,'data':serialized.data})

            return Response({'Error': True, 'Message':serialized.errors,'Status': 500,'data':[]})

        except ObjectDoesNotExist:
            return Response({'Error': True, 'Message':"Not Found",'Status': 500,'data':[]})

        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def get_apperalsize(self, request):
        """ Get list of ApperalSize
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            asize = ApparelSize.objects.all()
            serializer = ApparelSizeSerializer(asize, many=True)
            return Response({'Error': False, 'Message':'ApperalSize Data','Status': 200,'data':serializer.data})

        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def delete_apperalsize(self, apperalsize_id):
        """Delete color
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            asize = ApparelSize.objects.get(pk=apperalsize_id)
            asize.delete()

            # Rollback db transaction if exception is thrown
            with transaction.atomic():
                asize.save()
                serialized = ApparelSizeSerializer(asize)
            return Response({'Error': False, 'Message':'ApperalSize Delete Successfully','Status': 200,'data':[]})
        except ObjectDoesNotExist:
            return Response({'Error': True, 'Message':"Not Found",'Status': 500,'data':[]})


# Bussniess Logic for ProductCategories


    def create_productcategory(self, payload_data):
        """Create a productcategory
        Returns:
            [dict]: [Message Object with keys: status, error,
                                    message and data]
        """
        try:
            serialized = ProductCategoriesSerializer(data=payload_data)

            if serialized.is_valid(raise_exception=True):

                # Rollback db transaction if exception is thrown
                with transaction.atomic():

                    productcategory = serialized.save()
                    serialized_productcategory = ProductCategoriesSerializer(productcategory)

                return Response({'Error': False, 'Message':'ProductCategories Created!!','Status': 200,'data':serialized_productcategory.data})
        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def get_productcategory(self, request):
        """ Get list of productcategory
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            productcategory = ProductCategories.objects.all()
            serializer = ProductCategoriesSerializer(productcategory, many=True)
            return Response({'Error': False, 'Message':'productcategory Data','Status': 200,'data':serializer.data})

        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def delete_productcategory(self, productcategories_id):
        """Delete color
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            productcategory = ProductCategories.objects.get(pk=productcategories_id)
            print(productcategory)
            productcategory.delete()

            # Rollback db transaction if exception is thrown
            with transaction.atomic():
                serialized = ProductCategoriesSerializer(productcategory)
            return Response({'Error': False, 'Message':'Productcategory Delete Successfully','Status': 200,'data':[]})
        except ObjectDoesNotExist:
            return Response({'Error': True, 'Message':"Not Found",'Status': 500,'data':[]})

# Bussniess Logic for ProductColor

    def create_productcolor(self, payload_data):
        """Create a productcolor
        Returns:
            [dict]: [Message Object with keys: status, error,
                                    message and data]
        """
        try:
            serialized = ProductColorSerializer(data=payload_data)

            if serialized.is_valid(raise_exception=True):

                # Rollback db transaction if exception is thrown
                with transaction.atomic():

                    productcolor = serialized.save()
                    serialized_productcolor = ProductColorSerializer(productcolor)

                return Response({'Error': False, 'Message':'ProductColor Created!!','Status': 200,'data':serialized_productcolor.data})
        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def get_productcolor(self, request):
        """ Get list of productcolor
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            productcolor = ProductColor.objects.all()
            serializer = ProductColorSerializer(productcolor, many=True)
            return Response({'Error': False, 'Message':'Product Color Data','Status': 200,'data':serializer.data})

        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def delete_productcolor(self, productcolor_id):
        """Delete productcolor
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            productcolor = ProductColor.objects.get(pk=productcolor_id)
            productcolor.delete()

            # Rollback db transaction if exception is thrown
            with transaction.atomic():
                productcolor.save()
                serialized = ProductColorSerializer(productcolor)
            return Response({'Error': False, 'Message':'Product Color Delete Successfully','Status': 200,'data':[]})
        except ObjectDoesNotExist:
            return Response({'Error': True, 'Message':"Not Found",'Status': 500,'data':[]})

# Busniess Logic for ProducthasColor

    def create_producthascolor(self, payload_data):
        """Create a producthascolor
        Returns:
            [dict]: [Message Object with keys: status, error,
                                    message and data]
        """
        try:
            serialized = ProductHasColorsSerializer(data=payload_data)

            if serialized.is_valid(raise_exception=True):

                # Rollback db transaction if exception is thrown
                with transaction.atomic():

                    producthascolor = serialized.save()
                    serialized_producthascolor = ProductHasColorsSerializer(producthascolor)

                return Response({'Error': False, 'Message':'ProductHasColor Created!!','Status': 200,'data':serialized_producthascolor.data})
        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def get_producthascolor(self, request):
        """ Get list of producthascolor
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            producthascolor = ProductHasColors.objects.all()
            serializer = ProductHasColorsSerializer(producthascolor, many=True)
            return Response({'Error': False, 'Message':'ProducdHasColor Data','Status': 200,'data':serializer.data})

        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def delete_productcolor(self, producthascolor_id):
        """Delete productcolor
        Returns:
            [dict]: [Message Object with keys: status, error, message and data]
        """
        try:
            producthascolor = ProductHasColors.objects.get(pk=producthascolor_id)
            producthascolor.delete()
            return Response({'Error': False, 'Message':'ProducthasColor Delete Successfully','Status': 200,'data':[]})
        except ObjectDoesNotExist:
            return Response({'Error': True, 'Message':"Not Found",'Status': 500,'data':[]})