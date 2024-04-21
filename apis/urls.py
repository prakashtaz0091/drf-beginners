from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')


schema_view = get_schema_view(
    openapi.Info(
        title="Products API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.home, name="home"),
    path('class-based/', views.HomeView.as_view(), name="class-based"),
    # path('products/', views.ProductList.as_view(), name="products"),
    # path('add-product/', views.AddProduct.as_view(), name="add-product"),
    # path('products/', views.ProductView.as_view(), name="products"),
    # path('product/<int:pk>/', views.ProductDetail.as_view(), name="product"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + router.urls