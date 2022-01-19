from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.models import Product, Category, Brand, Review, RecommendedProduct
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer, ReviewSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/products',
        'GET /api/products/:id',
        'GET /api/categories',
        'GET /api/brands',
        'GET /api/reviews/:id',
        'GET /api/recommended-products',
    ]
    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBrands(request):
    brands = Brand.objects.all()
    print(brands)
    serializer = BrandSerializer(brands, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getReviews(request, pk):
    product = Product.objects.get(id=pk)
    reviews = Review.objects.filter(product=product)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRecommendedProducts(request):
    recommended_products = RecommendedProduct.objects.all()
    if recommended_products:
        recommended_products = recommended_products[0].product.all()
    else:
        recommended_products = []
    serializer = ProductSerializer(recommended_products, many=True)
    return Response(serializer.data)
