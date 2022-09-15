from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def querying(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
    'list_item': data_katalog_item,
    'name': 'Dylan',
    'studentid' : '2106720872',
    }
    return render(request, "katalog.html", context)
    