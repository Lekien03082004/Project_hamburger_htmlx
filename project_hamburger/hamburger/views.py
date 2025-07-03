from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import *


# Create your views here.
def logInView(request):
    pass


def logOutView(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("home")
    


def homeView(request):
    list = ItemList.objects.all()
    items = Items.objects.all()
    reviews = FeedBack.objects.all()
    return render(request, "home.html", {"list": list, "items": items, "review": reviews})


def aboutView(request):
    data = AboutUs.objects.all()
    return render(request, "about.html", {"data": data})


def MenuView(request):
    list = ItemList.objects.all()
    items = Items.objects.all()
    return render(request, "menu.html", {"list": list, "items": items})


def bookTableView(request):
    if request.method == "POST":
        name = request.POST.get("user_name")
        email = request.POST.get("user_email")
        phone_number = request.POST.get("phone_number")
        booking_date = request.POST.get("booking_data")
        total_person = request.POST.get("total_person")
        
        if(name != "" and email != "" and phone_number != "" and booking_date != ""):
            data = BookTable(
                Name=name,
                Email=email,
                Phone=phone_number,
                Booking_date=booking_date,
                Total_persons=total_person,
            )
            print(data)
            data.save()
        
    return render(request, "book_table.html")


def feedBackView(request):
    return render(request, "feedback.html")
