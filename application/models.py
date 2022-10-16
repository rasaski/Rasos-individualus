from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True)


class FoodMaker(models.Model):
    brand = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'FoodMaker'
        verbose_name_plural = 'FoodMakers'


class FoodConsistence(models.Model):
    consistence = models.CharField(max_length=3, null=False, blank=False)

    class Meta:
        verbose_name = 'FoodConsistence'
        verbose_name_plural = 'FoodConsistences'


class AvailableWeight(models.Model):
    weight = models.FloatField()

    class Meta:
        verbose_name = 'AvailableWeight'
        verbose_name_plural = 'AvailableWeights'


class FoodName(models.Model):
    food_maker = models.ForeignKey(FoodMaker, on_delete=models.CASCADE, null=False, blank=False)
    food_names = models.CharField(max_length=50, null=False, blank=False)
    food_consistence = models.ForeignKey(FoodConsistence, on_delete=models.CASCADE, null=True, blank=True)
    available_weight = models.ForeignKey(AvailableWeight, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField('Photo', upload_to='foods', null=True, blank=True)
    info = HTMLField('Info', null=True, blank=True)

    class Meta:
        verbose_name = 'FoodName'
        verbose_name_plural = 'FoodNames'
