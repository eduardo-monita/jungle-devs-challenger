from django.utils.safestring import mark_safe

from rest_framework import serializers

from posts.models import Author, Article

class AdminAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'name', 'picture', 'active','created_at', 'updated_at']

class AdminArticleSerializer(serializers.ModelSerializer):
    author = AdminAuthorSerializer(many=False, required=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'category', 'summary', 'author', 'active', 'first_paragraph', \
                  'body', 'created_at', 'updated_at']

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'name', 'picture']

class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, required=True)
    first_paragraph = serializers.SerializerMethodField()
    body = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'summary', 'first_paragraph', 'body']

    def to_representation(self, obj):
        article = super(ArticleSerializer, self).to_representation(obj)
        if article['first_paragraph'] == '':
            del article['first_paragraph']
        if article['body'] == '':
            del article['body']
        return article

    def get_first_paragraph(self, obj):
        request = self.context.get('request')
        if 'pk' in request.parser_context['kwargs']:
            return mark_safe(obj.first_paragraph)
        return ''

    def get_body(self, obj):
        request = self.context.get('request')
        if not str(request.user) == 'AnonymousUser':
            return mark_safe(obj.body)
        return ''

