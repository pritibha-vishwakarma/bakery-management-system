from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.add_order, name='add_order'),
    path('orders/edit/<int:id>/', views.edit_order, name='edit_order'),
    path('orders/delete/<int:id>/', views.delete_order, name='delete_order'),
]