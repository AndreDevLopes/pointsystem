"""pointsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from knox import views as knox_views
from django.contrib import admin
from django.urls import path, include
from .views import ping, LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', ping, name="ping"),
    path('api/ponto/', include('ponto.urls'), name='ponto'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/servidor/', include('servidor.urls'), name='servidor'),
    path('api/feriado/', include('feriado.urls'), name='feriado')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
