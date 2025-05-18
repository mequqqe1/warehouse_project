from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet,
    ProductCategoryViewSet,
    SupplierViewSet,
    PurchaseOrderViewSet,
    PurchaseItemViewSet
)
from .views import StockEntryViewSet

router = DefaultRouter()
router.register(r'categories', ProductCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'orders', PurchaseOrderViewSet)
router.register(r'items', PurchaseItemViewSet)
router.register(r'entries', StockEntryViewSet, basename='entries')

urlpatterns = [
    path('', include(router.urls)),
]