from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, index

app_name = 'electric_shop_app'

urlpatterns = [
    path('', index, name='index'),  # Обернуто внутри списка urlpatterns
]

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet, basename='supplier')
urlpatterns += router.urls
