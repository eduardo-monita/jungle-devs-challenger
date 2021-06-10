from django.conf.urls import include, url

from rest_framework import routers

from posts.views import (
    AdminAuthorViewSet,
    AdminArticleViewSet,
    ArticleViewSet,
)

router = routers.DefaultRouter()
router.register(r'api/admin/authors', AdminAuthorViewSet)
router.register(r'api/admin/articles', AdminArticleViewSet)
router.register(r'api/articles', ArticleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]