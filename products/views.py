from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product, Category, Review
from products.serializers import ProductSerializers, CategorySerializers, ReviewSerializers, ProductReviewSerializers


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        serializer = ProductSerializers(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        queryset = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializers(queryset).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ProductSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == "GET":
        queryset = Category.objects.all()
        serializer = CategorySerializers(queryset, many=True).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        queryset = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategorySerializers(queryset).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = CategorySerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == "GET":
        queryset = Review.objects.all()
        serializer = ReviewSerializers(queryset, many=True).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ReviewSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        queryset = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializers(queryset).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ReviewSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def product_review_list_api_view(request):
    queryset = Product.objects.all()
    serializer = ProductReviewSerializers(queryset, many=True).data
    return Response(data=serializer, status=status.HTTP_200_OK)