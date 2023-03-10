from django.urls import path

from . import views

app_name = 'shoppinglist'
urlpatterns = [
    path("<int:shoplist_id>", views.index, name="shoplist"),
    path("add_item/<int:shoplist_id>", views.add_item, name="addItem")
]