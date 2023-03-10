from django.shortcuts import render
from .models import Shoplist, Item
from .forms import AddItemForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request, shoplist_id):
    slist = Shoplist.objects.get(pk=shoplist_id)
    s_list = Shoplist.objects.values_list("title", flat=True)
    items = Item.objects.filter(shoplist=shoplist_id).order_by("item_name")
    ctx = {'list': slist, 'item': items, 'shoplist_id': shoplist_id, "allshops": s_list}
    return render(request, 'base.html', context=ctx)

def add_item(request, shoplist_id):
    submitted = False
    if request.method == "POST":
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/shoplist/{shoplist_id}?submitted=True')
    else:
        form = AddItemForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'addItem.html', {'form': form,'shoplist_id': shoplist_id, 'submitted': submitted})
