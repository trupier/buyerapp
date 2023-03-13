from django.shortcuts import render, get_object_or_404
from .models import Shoplist, Item
from .forms import AddItemForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request, shoplist_id):
    slist = get_object_or_404(Shoplist, id=shoplist_id)
    alllist = Shoplist.objects.all()
    items = Item.objects.filter(shoplist=slist).order_by("item_name")
    ctx = {'slist': slist, 'items': items, 'shoplist_id': shoplist_id, 'alllist': alllist}
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
