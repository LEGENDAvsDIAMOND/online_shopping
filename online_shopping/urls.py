"""
URL configuration for online_shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from customer.views import CustomerViewSet
from shopcard.views import ShopCardViewSet
from items.views import ItemViewSet
from product.views import ProductViewSet
from category.views import CategoryViewSet
from shopcard.views import purchase_history
from shopcard.views import purchase_history, check_purchase_total
from product.views import total_product_amount, expired_products, best_selling_product
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Online Shopping API",
        default_version="v1",
        description="API documentation for the Online Shopping project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'shopcards', ShopCardViewSet)
router.register(r'items', ItemViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/purchase-history/', purchase_history, name='purchase-history'),
    path('api/purchase-history/<int:user_id>/', purchase_history, name='purchase-history-user'),
    path('api/check-purchase-total/<int:customer_id>/', check_purchase_total, name='check_purchase_total'),
    path('api/total-product-amount/', total_product_amount, name='total_product_amount'),
    path('api/expired-products/', expired_products, name='expired_products'),
    path('api/best-selling-product/', best_selling_product, name='best_selling_product'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

