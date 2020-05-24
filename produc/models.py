from django.db import models

# Create your models here.
class products(models.Model):
    title       = models.CharField(max_length=120,)
    discription = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    summary     = models.TextField(blank=False, null=False)
    futured     = models.BooleanField()