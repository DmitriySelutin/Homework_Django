from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, CatalogProductListView, CatalogProductDetailView, CatalogProductCreateView, \
    CatalogProductUpdateView, CatalogProductDeleteView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/", CatalogProductListView.as_view(), name="product_list"),
    path("product/<int:pk>", CatalogProductDetailView.as_view(), name="product_detail"),
    path("create/", CatalogProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", CatalogProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", CatalogProductDeleteView.as_view(), name="product_delete")
]
