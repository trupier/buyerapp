# Generated by Django 4.1.7 on 2023-03-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplist', '0004_item_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(help_text='Enter your item name here', max_length=200),
        ),
    ]