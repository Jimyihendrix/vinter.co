from django.urls import path 
from . import views
# rest_framework
from rest_framework.authtoken.views import obtain_auth_token # rest_framewor.authtoken




urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # api-token-auth
]
