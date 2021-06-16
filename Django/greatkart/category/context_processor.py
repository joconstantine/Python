from .models import Category


def category_menu_links(request):
    links = Category.objects.all()
    return dict(category_links=links)
