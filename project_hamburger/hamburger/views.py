from django.shortcuts import render

from .models import *


# Create your views here.
def logInView(request):
    pass


def logOutView(AuthLoginView):
    pass


def homeView(request):
    list = ItemList.objects.all()
    items = Items.objects.all()
    reviews = FeedBack.objects.all()
    return render(request, "home.html", {"list": list, "items": items, "review": reviews})


def aboutView(request):
    return render(request, "about.html")


def MenuView(request):
    list = ItemList.objects.all()
    items = Items.objects.all()
    return render(request, "menu.html", {"list": list, "items": items})


def bookTableView(request):
    return render(request, "book_table.html")


def feedBackView(request):
    return render(request, "feedback.html")
