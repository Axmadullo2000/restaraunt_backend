from django.db import models
class Restorans(models.Model):
    name = models.TextField()
    adress = models.TextField()
    phone = models.TextField()
    rate = models.TextField()
    range_money = models.TextField()
    type_cook = models.TextField()
    photo_one = models.TextField()
    photo_two = models.TextField()
    def __str__(self):
        return self.name


# Create your models here.
