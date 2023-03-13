"""hh_test URL Configuration

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
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.contrib import admin
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from enterprise.views import Home, MyVacancy, PutchVacancy, DeleteVacancy
from client.views import Client, DelitClien, PutchClient, ImClient, FollowViewSet
v1_router = DefaultRouter()


v1_router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('admin/', admin.site.urls), #
    path('home', Home.as_view({'get': 'list'})), #
    path('home/patch/<int:pk>', PutchVacancy.as_view()), #
    path('home/del/<int:pk>', DeleteVacancy.as_view()), #
    path('home/my', MyVacancy.as_view()), #
    path('HomeHm/del/<int:pk>', DelitClien.as_view()), #
    path('HomeHm', Client.as_view({'get': 'list'})), #
    path('HomeHm/my', ImClient.as_view()), #
    path('HomeHm/patch/<int:pk>', PutchClient.as_view()), #
    path('v1/', include(v1_router.urls)), #
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #
    # path('drf-auth/', include('rest_framework.urls')), #
    #path('auth/', include('djoser.urls')), #
    #path('auth/', include('djoser.urls.authtoken')), #
]
