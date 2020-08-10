from django.shortcuts import render, redirect
from .models import MenuItem, Course
import logging

logger = logging.getLogger(__name__)
# Create your views here.
 
def index(request): #the index view
    menuItems = MenuItem.objects.all() #querying all menu items with the object manager
    courses = Course.objects.all()

    apps = MenuItem.objects.filter(course=Course.objects.get(name="Appetizer"))
    entrees = MenuItem.objects.filter(course=Course.objects.get(name="Entree"))
    desserts = MenuItem.objects.filter(course=Course.objects.get(name="Dessert"))
    sides = MenuItem.objects.filter(course=Course.objects.get(name="Sides"))
    drinks = MenuItem.objects.filter(course=Course.objects.get(name="Drinks"))
    
    for item in menuItems:
        item.p_formatter()
        logger.info(type(item.price)) # Logging the type of item.price
        logger.info(item.price) # Logging the value of item.price
        logger.info(type(item.output_price)) # Logging the type of item.output_price
        logger.info(item.output_price) # Logging the value of item.output_price
        item.save()
        
    if (request.method == "POST"): #checking if the request method is a POST
        if ("itemAdd" in request.POST): #checking if there is a request to add a menu item 
            dish_title = request.POST["dishTitle"]
            price = request.POST["price"]
            course = request.POST["course"]
            description = request.POST["description"]
            current_menu_item = MenuItem(dish_title=dish_title, price=price, course=Course.objects.get(name=course), description=description)
            current_menu_item.save() #saving the menu item
            return redirect("/") #reloading the page

 
    return render(request, "index.html", {"menuItems": menuItems, 
                                            "courses": courses,
                                            "apps": apps,
                                            "entrees": entrees,
                                            "desserts": desserts,
                                            "sides": sides,
                                            "drinks":drinks,
                                            }
                )
