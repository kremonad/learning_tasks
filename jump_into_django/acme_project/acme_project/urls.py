"""acme_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  
    # Если на сервер пришёл запрос к главной странице,
    # Django проверит на совпадение с запрошенным URL 
    # все path() в файле urls.py приложения homepage.
    path('', include('homepage.urls')),

    # Если в приложении homepage не найдётся совпадений,
    # Django продолжит искать совпадения здесь, в корневом файле urls.py.

    # Если запрос начинается с catalog/, 
    # Django будет искать совпадения в файле urls.py
    # приложения catalog.
    path('catalog/', include('catalog.urls')),
]
