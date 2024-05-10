from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, WorkViewSet, ReviewViewSet, PortfolioViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'works', WorkViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'portfolios', PortfolioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
