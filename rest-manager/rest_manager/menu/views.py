from django.shortcuts import render, redirect
from .models import MenuItem
 
# Create your views here.
 
def index(request): #the index view
    menuItems = MenuItem.objects.all() #querying all todos with the object manager
    
    if (request.method == "POST"): #checking if the request method is a POST
        if ("itemAdd" in request.POST): #checking if there is a request to add a todo
            dish_title = request.POST["itemName"]
            price = request.POST["price"]
            category = request.POST["menuItem"]
            description = request.POST["description"]
            current_menu_item = MenuItem(dishTitle=dish_title, price=price, category=category, description=description)
            current_menu_item.save() #saving the todo
            return redirect("/") #reloading the page

 
  return render(request, "index.html", {"menuItems": menuItems})