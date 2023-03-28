from products.models import Products, Category
from extras.models import HeroPage

def product_list(request):
    return {
        "hero_pages": HeroPage.objects.filter(is_displayed=True),
        "categories_header": Category.objects.filter(is_displayed_header=True),
        "categories_trending": Category.objects.filter(is_displayed_in_trending=True),
        "categories": Category.objects.all(),
        # "products":Products.objects.all(),
        # "products_liked":Products.objects.filter(is_liked=True)[::-1][0:5]
        }