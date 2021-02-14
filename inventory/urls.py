from django.contrib import admin
from django.urls import path

from .views import getItems, getItem, addItem, deleteItem

urlpatterns = [
    path('', getItems, name='items'),
    path('<int:pk>/', getItem, name='item'),
    path('add/', addItem, name='add-item'),
    path('<int:pk>/delete/', deleteItem, name='delete-item'),
]
