from django.urls import path
from products import views

urlpatterns = [
    path('products/', views.ProductsView.as_view()),
    path('products/<int:id>', views.ProductsView.as_view()),
]