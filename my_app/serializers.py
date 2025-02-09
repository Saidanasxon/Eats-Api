from rest_framework import serializers
from .models import * 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Food
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'

