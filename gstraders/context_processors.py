from products.models import Products


def product_list(request):
    return {"products":Products.objects.all()}