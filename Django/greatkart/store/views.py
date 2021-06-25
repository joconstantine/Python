from carts.models import CartItem
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from .models import Product
from category.models import Category
from carts.views import _cart_id

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = (
            Product.objects.all()
            .filter(category=categories, is_available=True)
            .order_by("id")
        )
    else:
        products = Product.objects.all().filter(is_available=True).order_by("id")

    paginator = Paginator(products, 3)
    page = request.GET.get("page")
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {"products": paged_products, "product_count": product_count}

    return render(request, "store/store.html", context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            slug=product_slug, category__slug=category_slug
        )
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=single_product
        ).exists()

        print(single_product.variations.colors)

    except Exception as e:
        raise e

    context = {
        "single_product": single_product,
        "in_cart": in_cart,
    }
    return render(request, "store/product-detail.html", context)


def search(request):
    if "keyword" in request.GET:
        keyword = request.GET.get("keyword")
        if keyword:
            products = Product.objects.order_by("created_date").filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
            )

    context = {
        "products": products,
        "product_count": products.count(),
    }
    return render(request, "store/store.html", context)
