from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from posts.models import Author, Article
from posts.serializers import (
    AdminAuthorSerializer, 
    AdminArticleSerializer,
    ArticleSerializer,
)

@permission_classes([IsAdminUser])
class AdminAuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.filter(active=True)
    serializer_class = AdminAuthorSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

@permission_classes([IsAdminUser])
class AdminArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(active=True)
    serializer_class = AdminArticleSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

@permission_classes([AllowAny])
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(active=True)
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    http_method_names = ['get']

    def list(self, request):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            queryset = self.get_queryset()
            article = get_object_or_404(queryset, pk=pk)
            serializer = self.get_serializer(article, many=False)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)