from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import AccountViewSet

router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')

app_name= 'accounts'

urlpatterns = [
    path('', include(router.urls)),
]

