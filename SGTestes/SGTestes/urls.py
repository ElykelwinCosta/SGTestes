from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('home/')),
    path('admin/', admin.site.urls, name='admin'),
    path('home/', include('home.urls')),
    path('users/', include('users.urls')),
    path('testscenarios/', include('testScenarios.urls')),
    path('requirements/', include('requirements.urls')),
    path('reports/', include('reports.urls')),
    path('dashboards/', include('dashboards.urls')),
]

# Adicionar a rota para servir os arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)