from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="श्रेणीचे नाव")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "श्रेणी"
        verbose_name_plural = "श्रेणी"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="उत्पादनाचे नाव")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="श्रेणी"
    )
    description = models.TextField(blank=True, verbose_name="वर्णन")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="किंमत"
    )
    stock = models.PositiveIntegerField(default=0, verbose_name="साठा")
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="उत्पादनाचा फोटो"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="तयार केले"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "उत्पादन"
        verbose_name_plural = "उत्पादने"