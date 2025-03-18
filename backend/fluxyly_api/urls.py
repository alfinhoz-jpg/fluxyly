from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet, ClienteViewSet, ReservaViewSet
from .auth_views import RegisterView, LoginView  # <-- Verificar se está correto!

print("🚀 RegisterView carregada com sucesso!")  # <-- Adicionando print para teste

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/register/', RegisterView.as_view(), name='register'),  
    path('api/auth/login/', LoginView.as_view(), name='login'),  
]
