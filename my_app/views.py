from .serializers import *
from .models import *
from .permissions import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, BaseAuthentication, SessionAuthentication

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermission]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [CustomPermission]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CustomPermission]
    authentication_classes = [BaseAuthentication, SessionAuthentication]


