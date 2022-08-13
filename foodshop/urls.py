"""foodshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product.views import homepage, Category, categories_info, register, PricingListView, PricingDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('categories/', Category, name="category"),
    # path('buy/', Buy, name="buy"),
    path('categories/<id>/', categories_info),
    path('registration/', register, name="register"),
    path('buy/', PricingListView.as_view(), name='buy'),
    path('registration/', register, name="register"),
    path('buy/<pk>/', PricingDetailView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+\
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
