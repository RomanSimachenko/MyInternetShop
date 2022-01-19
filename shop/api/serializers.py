from rest_framework.serializers import ModelSerializer
from shop.models import Product, Category, Brand, Review, RecommendedProduct


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
