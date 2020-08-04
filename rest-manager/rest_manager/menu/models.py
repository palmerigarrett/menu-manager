from django.db import models
from django.utils import timezone

class MenuItem(models.Model): # MenuItem Class inherits models.Model
    dishTitle = models.CharField(max_length=250) # a varchar
    price = models.IntegerField(default=0) # an integer field
    description = models.TextField(blank=True) # a text field
    course = models.CharField(max_length=100)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date

    class Meta:
        ordering = ["dishTitle"] #ordering by the created field

    def __str__(self):
       return self.dishTitle #name to be shown when called