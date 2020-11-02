from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Breed(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Insert a cat breed (e.g. Persian)',
        validators=[MinLengthValidator(2, 'Your breed name must have at least 2 characters.')]
    )

    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, 'Your cat nickname must have at least 2 characters')]
    )
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=300)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nick