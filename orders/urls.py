from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/<int:flavor_id>/', views.order_view, name='order'),
]