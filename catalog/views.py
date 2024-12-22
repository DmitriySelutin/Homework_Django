from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


def home(request):
    """Контроллер для домашней страницы."""
    return render(request, "catalog/home.html")


class CatalogProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "product_list"


class ContactsView(View):
    @staticmethod
    def get(request):
        return render(request, 'catalog/contacts.html')

    @staticmethod
    def post(request):
        name = request.POST.get('name')
        massage = request.POST.get('massage')
        return HttpResponse(f"Спасибо, {name}. Сообщение получено.")


class CatalogProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class CatalogProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:product_list")


class CatalogProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy("catalog:product_list")


    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class CatalogProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
