from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet, ClienteViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
