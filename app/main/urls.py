"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import AllowAny

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordChangeView

# from main.views import CustomAuthToken

admin.autodiscover()
admin.site.enable_nav_sidebar = False

schema_view = get_schema_view(
   openapi.Info(
      title="Posts API",
      default_version='v1',
      description="Post api documentation using swagger and redoc \n To Authorize `Token $token(result from /api/login/)`",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="eduardo.monita.dias@gmail.com"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns = [
    path('', RedirectView.as_view(url='/swagger/')),
    path('accounts/login/', RedirectView.as_view(url='/api/login/')),
    path('accounts/logout/', RedirectView.as_view(url='/api/sign-up/')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('posts.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^api/login/$', LoginView.as_view(), name='rest_login'),
    url(r'^api/sign-up/$', LogoutView.as_view(), name='rest_sign-up'),
    url(r'^api/user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^api/password/change/$', PasswordChangeView.as_view(), name='rest_password_change'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)