from django.db import models

# Create your models here.
class Shoplist(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default='Shopping List')
    #user_id = models.IntegerField()

class Item(models.Model):
    shoplist = models.ForeignKey(Shoplist, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    is_taken = models.BooleanField(default=False)

