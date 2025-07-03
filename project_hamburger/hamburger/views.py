from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import *


# Create your views here.
class logInView(AuthLoginView):
    template_name = "login.html"
    def get_success_url(self):
        # Kiem tra xem user co phai admin khong
        if self.request.user.is_staff:
            return reverse_lazy("admin:index")
        return reverse_lazy("home")



def logOutView(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("home")
    
def SignUpView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect("home")
        else:
            messages.error(request, "Error during signup. Please try again.")
    else:
        form = UserCreationForm()
        return render(request, "login.html", {"form": form, "tab": 'sigup'} )

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
