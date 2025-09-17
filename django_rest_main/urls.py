"""
URL configuration for django_rest_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
     # Web application endpoints:
     # These URLs handle the pages and features people use through their browsers.
     # For example, the 'students/' path loads the students app, showing HTML pages, forms, etc.
    path('students/', include('students.urls')),
    #API endpoints:
    # These URLs provide data and services that other programs or apps can use,
    # usually returning data in formats like JSON.
    # APIs allow different software to communicate with your application
    path('api/v1/', include('api.urls')),

]
