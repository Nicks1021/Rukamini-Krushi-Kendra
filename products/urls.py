from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("owner-login/", views.owner_login, name="owner_login"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("add-product/", views.add_product, name="add_product"),
    
    path(
    "add-category/",
    views.add_category,
    name="add_category"
),

    path(
        "edit-product/<int:product_id>/",
        views.edit_product,
        name="edit_product"
    ),
    
    path(
    "delete-product/<int:product_id>/",
    views.delete_product,
    name="delete_product"
),

    path("owner-logout/", views.owner_logout, name="owner_logout"),
]