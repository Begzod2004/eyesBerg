from rest_framework import serializers
from .models import Category, Work, Review, Portfolio, WorkImage

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'type']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']


class WorkImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkImage
        fields = ['id', 'image']

class WorkSerializer(serializers.ModelSerializer):
    images = WorkImageSerializer(many=True, read_only=True)
    class Meta:
        model = Work
        fields = ['id', 'user', 'title', 'description', 'location', 'price', 'start_date', 'payment_type', 'images']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'work', 'description', 'stars']

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'user', 'image', 'work', 'category']
