from django.urls import path

from . import views

urlpatterns = [
    path("", views.homeView, name="home"),
    path('login', views.logInView.as_view(), name="login"),
    path('logout', views.logOutView, name="logout"),
    path("signup", views.SignUpView, name="signup"),
    path("book_table", views.bookTableView, name="book_table"),
    path("menu", views.MenuView, name="menu"),
    path("about", views.aboutView, name="about"),
    path("feedback", views.feedBackView, name="feedback_form"),
]
