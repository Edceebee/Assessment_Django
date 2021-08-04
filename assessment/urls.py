from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers

from user.views import distance_view

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'distance', U)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', distance_view.as_view()),
]





