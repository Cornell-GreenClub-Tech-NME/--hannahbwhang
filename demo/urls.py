from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.user_route, name='users'),
    path('api/users/transactions/', views.transaction_route, name='transactions')
]