from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Empresa, Cliente, Reserva
from .serializers import EmpresaSerializer, ClienteSerializer, ReservaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.AllowAny]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.AllowAny]


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer_instance):
        
        if hasattr(self.request.user, 'cliente'):
            serializer_instance.save(cliente=self.request.user.cliente)
        else:
            return Response(
            {"error": "Usuário não possui um perfil de cliente"},
            status=status.HTTP_400_BAD_REQUEST
        )