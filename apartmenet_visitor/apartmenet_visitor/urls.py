"""apartmenet_visitor URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from visitors import views
from apartmenet_visitor import settings
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "NRI City"
admin.site.site_title = "NRI City"
admin.site.index_title = "Welcome to NRI City"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView, name='index'),
    path('register',views.register_request , name='register'),
    path('login' , views.login_request , name='login'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

