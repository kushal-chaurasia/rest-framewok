from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Card (models.Model):
    transaction = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    expiry = models.DateField()
    number = models.IntegerField(validators=[MaxValueValidator(9999999999999999)])
    cvv = models.IntegerField(validators=[MaxValueValidator(999)])

    def __str__(self):
        return self.name
