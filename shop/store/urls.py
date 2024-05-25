from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('category/<slug:slug>/', CategoryList.as_view(), name='category_detail'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('login_registration/', login_registration, name='login_registration'),
]
