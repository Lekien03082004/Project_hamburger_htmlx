from django.urls import path

from . import views

urlpatterns = [
    path("", views.homeView, name="home"),
    path('logout', views.logOutView, name="logout"),
    path("book_table", views.bookTableView, name="book_table"),
    path("menu", views.MenuView, name="menu"),
    path("about", views.aboutView, name="about"),
    path("feedback", views.feedBackView, name="feedback_form"),
    path("login", views.logInView, name="login"),
    path("logout", views.logOutView, name="logout"),
]
