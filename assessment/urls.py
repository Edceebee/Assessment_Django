from django.urls import path, include

from user.views import distance_view

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('solution/', distance_view.as_view()),
]





