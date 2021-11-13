from django.urls import path
from products_filter import views

urlpatterns = [
    path("products_filter", views.ProductsFilterView.as_view()),
    path("products_order", views.ProductsOrderView.as_view()),
    path("products_search", views.ProductsSearchView.as_view()),
]
