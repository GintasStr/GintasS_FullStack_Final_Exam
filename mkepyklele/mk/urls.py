from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('blog/', blog, name="blog"),
    path('blog/<int:pk>', blogPost, name="blogPost"),
    path('products/', products, name="products"),
    path('contacts/', contacts, name="contacts"),
    path('products/<str:slug>', showProducts, name="showProducts"),
]