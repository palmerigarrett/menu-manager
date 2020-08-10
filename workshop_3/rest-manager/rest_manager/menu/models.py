from django.db import models
from django.utils import timezone

class Course(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
       verbose_name = ("Course")
       verbose_name_plural = ("Courses")

    def __str__(self): # _str_ method will specify what to return when you call str() on an object
       return self.name
    

class MenuItem(models.Model): # MenuItem Class inherits models.Model
    dish_title = models.CharField(max_length=250) # a varchar
    price = models.FloatField(default=0) # a float field
    description = models.TextField(blank=True) # a text field
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    output_price = models.CharField(max_length=250) # a varchar

    class Meta:
        ordering = ["dish_title"] #ordering by the created field

    def __str__(self):
       return self.dish_title #name to be shown when called

    def p_formatter(self):
        self.output_price = "{:.2f}".format(round(self.price, 2))
        