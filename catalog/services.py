from django.core.cache import cache

from config.settings import CACHES_ENABLED

from catalog.models import Product

def get_products_from_cache():
    """Получает данные по продуктам из кэша,если кэш пуст,то получает из БД"""
    if not CACHES_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

