"""
urls for product app
"""

from django.urls import path
from .views import ProductViewset, CategoriesViewset, ColorViewset, ApparelSizeViewset, ProductCategoriesViewset, ProductColorViewset, ProductHasColorViewset

urlpatterns = [
    # Product Create, Update,List, Delete url
    path('product/', ProductViewset.as_view({'post': 'create','patch': 'update','get': 'list',}),name='product'),
    path('product/<int:product_id>/', ProductViewset.as_view({'delete':'delete'}),name='del-product'),


    # Category Create, Update, List, Delete url
    path('category/', CategoriesViewset.as_view({'post': 'create','patch': 'update','get': 'list'}),name='category'),
    path('category/<int:category_id>/', CategoriesViewset.as_view({'delete':'delete'}),name='category'),


    # Color Create, Update, List, Delete url
    path('color/', ColorViewset.as_view({'post': 'create','patch': 'update','get': 'list'}),name='color'),
    path('color/<int:color_id>/', ColorViewset.as_view({'delete':'delete'}),name='color'),


    # ApperalSize Create, Update, List, Delete url
    path('apperalsize/', ApparelSizeViewset.as_view({'post': 'create','patch': 'update','get': 'list'}),name='color'),
    path('apperalsize/<int:apperalsize_id>/', ApparelSizeViewset.as_view({'delete':'delete'}),name='del-asize'),


    # Productcategory Create, Update, List, Delete url
    path('productcategory/', ProductCategoriesViewset.as_view({'post': 'create','patch': 'update','get': 'list'}),name='color'),
    path('productcategory/<int:productcategories_id>/', ProductCategoriesViewset.as_view({'delete':'delete'}),name='productcategories'),


    # ProductColor Create, Update, List, Delete url
    path('productcolor/', ProductColorViewset.as_view({'post': 'create','patch': 'update','get': 'list'}),name='color'),
    path('productcolor/<int:productcolor_id>/', ProductCategoriesViewset.as_view({'delete':'delete'}),name='del-productcolor'),


    # ProducthasColor Create, Update, List, Delete url
    path('producthascolor/', ProductHasColorViewset.as_view({'post': 'create','patch': 'update','get': 'list'}),name='color'),
    path('producthascolor/<int:producthascolor_id>/', ProductHasColorViewset.as_view({'delete':'delete'}),name='del-productcolor'),

]