from django.urls import path

from products import views
from products.views import (
    CategoryListAPIView,
    CategoryDetailAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    ReviewListAPIView,
    ReviewDetailAPIView,
    ProductReviewListAPIView
)

# urlpatterns = [
#     path('products/categories/', views.category_list_api_view),
#     path('products/categories/<int:id>/', views.category_detail_api_view),
#     path('products/products/', views.product_list_api_view),
#     path('products/products/<int:id>/', views.product_detail_api_view),
#     path('products/reviews/', views.review_list_api_view),
#     path('products/reviews/<int:id>/', views.review_detail_api_view),
#     path('products/products/reviews/', views.product_review_list_api_view)
# ]

urlpatterns = [
    path('products/categories/', CategoryListAPIView.as_view()),
    path('products/categories/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('products/products/', ProductListAPIView.as_view()),
    path('products/products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('products/reviews/', ReviewListAPIView.as_view()),
    path('products/reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('products/products/reviews/', ProductReviewListAPIView.as_view()),
]