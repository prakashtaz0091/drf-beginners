from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


#generics
from rest_framework import generics



#models
from .models import Product



#serializers
from .serializers import ProductSerializer


#viewsets
from rest_framework import viewsets

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING),
        'age': openapi.Schema(type=openapi.TYPE_INTEGER),
    }
))



@api_view(['GET', 'POST'])
def home(request):
    if request.method=='POST':
        print("hello")
        print(request.data)

    return Response({"message": "Hello World"}, status=200)




class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Hello World, this message is from class based view"})



    def post(self, request):
        print("this is post request", request.data)




# class ProductList(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class AddProduct(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    # product = Product.objects.get(pk = pk)
    serializer_class = ProductSerializer



class ProductViewSet(viewsets.ViewSet):
    """
    Information of products
    """
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk=None):
        queryset =Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=200)


    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



    def update(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=204)
