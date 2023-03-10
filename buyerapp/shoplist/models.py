from django.db import models

# Create your models here.
class Shoplist(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default='Shopping List')
    #user_id = models.IntegerField()
    def __str__(self):
        return self.title

class Item(models.Model):
    shoplist = models.ForeignKey(Shoplist, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200, help_text='Enter your item name here')
    is_taken = models.BooleanField(default=False)
    amount = models.IntegerField(default=1)
    #category = category will be placed here in the future
    def __str__(self):
        return self.item_name
