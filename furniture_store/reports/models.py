from django.db import models


class Shops(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name
