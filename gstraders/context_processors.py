from products.models import Products, Category


def product_list(request):
    return {
        "categories": Category.objects.all(),
        "products":Products.objects.all(),
        "products_liked":Products.objects.filter(is_liked=True)[::-1][0:5]
        }