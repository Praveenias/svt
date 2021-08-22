from django.db import models

# Create your models here.


class Details(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    model = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name