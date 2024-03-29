from django.db import models
from core.models import TimeStampedModel, Item, MetricSystem


# Create your models here.
class Stock(TimeStampedModel):
    name = models.CharField(max_length=128)
    brand = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, null=True)
    barcode = models.CharField(max_length=128, null=True, unique=True)
    quantity = models.FloatField(default=0)
    limit = models.FloatField(default=0)

    store_item_ref = models.ForeignKey(
        Item, null=True, on_delete=models.SET_NULL)
    # procurement_ref = models.ForeignKey('Purchase', null=True, on_delete=models.SET_NULL)

    metric_system = models.ForeignKey(
        MetricSystem, null=True, on_delete=models.SET_NULL)

    def export_to_sales_product(self):
        pass


class InStock(TimeStampedModel):
    quantity = models.IntegerField()
    stock_name = models.CharField(max_length=128)
    metric = models.CharField(max_length=128)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


class OutStock(TimeStampedModel):
    quantity = models.IntegerField()
    stock_name = models.CharField(max_length=128)
    metric = models.CharField(max_length=128)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


class StockCategory(TimeStampedModel):
    name = models.CharField(max_length=128)


class StockCategories(TimeStampedModel):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    category = models.ForeignKey(StockCategory, on_delete=models.CASCADE)
