from django.db import models
from diet.models import BaseModel
# Create your models here.

class Food(BaseModel):
    class Type(models.IntegerChoices):
        CARBOHYDRATE=1
        PROTEIN=2
        FAT=3
        FRUITS=4
        MILK=5
        VEGETABLES=6

    class TypeAmount(models.IntegerChoices):
        CUP=1
        GRAM=2
        PIECE=3
    name = models.CharField(max_length=30, unique=True)
    food_type =models.PositiveSmallIntegerField(choices=Type.choices)
    amount = models.PositiveSmallIntegerField(default=0)
    amout_type = models.PositiveSmallIntegerField(choices=TypeAmount.choices, default=2)
    calories = models.FloatField(max_length=30, default=0)
    protein = models.FloatField(max_length=30, default=0)
    fat = models.FloatField(max_length=30, default=0)
    carbohydrate = models.FloatField(max_length=30, default=0)
    calcium = models.FloatField(max_length=30, default=0)
    cholesterol = models.FloatField(max_length=30, default=0)
    iron = models.FloatField(max_length=30, default=0)
    sodium = models.FloatField(max_length=30, default=0)
    vitamin_C = models.FloatField(max_length=30, default=0)
    vitamin_A = models.FloatField(max_length=30, default=0)
    def __str__(self):
        return self.name
    