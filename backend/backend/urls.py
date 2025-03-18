from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fluxyly_api.urls')),  # Certifique-se de que essa linha está correta
]
