
from rest_framework import serializers
from .models import Category, Product
from review.serializers import ReviewSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data

        return rep

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'