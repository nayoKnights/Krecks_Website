from django.urls import path
from . import views
from .views import migrate_now

urlpatterns = [
    path('', views.home, name='home'),
    path('order/<int:flavor_id>/', views.order_view, name='order'),
    path('migrate-now/', migrate_now),
]