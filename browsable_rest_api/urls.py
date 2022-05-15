"""browsable_rest_api URL Configuration

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
from django.urls import path, include
from api.views import EmployeeModelViewSet, home_page, EmployeeViewSet, ApiTypeModelViewSet
from api import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('get', EmployeeModelViewSet, basename='employee')
router_2 = DefaultRouter()
router_2.register('get', EmployeeViewSet, basename='employee')
router_3 = DefaultRouter()
router_3.register('get', ApiTypeModelViewSet, basename='api-type')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home-page"),
    path('model-view-sets-based/', include(router.urls), name='model-view-sets-based'),
    path('api-type/', include(router_3.urls), name='api-type'),
    path('view-sets-based/', include(router_2.urls), name='view-sets-based'),
    path('generic-views-based/employee-data', views.EmployeeCreateAndList.as_view(), name='generic-views-based-get'),
    path('generic-views-based/employee-data/<int:pk>', views.EmployeeCreateAndList.as_view(), name='generic-views-based-modify'),
    path('function-based-api/employee-data/', views.function_based_api, name='function-based'),
    path('function-based-api/employee-data/<int:pk>/', views.function_based_api, name='function-based-with-id'),
]
