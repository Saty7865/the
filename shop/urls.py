#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="shophome"),
    path("about/", views.about, name="aboutus"),
    path("store/", views.index, name="store"),
    path("contact/", views.contact, name="contactus"),
    path("tracker/", views.tracker, name="trackingstatus"),
    path("search/", views.search, name="search"),
    path("products/<int:myid>", views.productview, name="viewproduct"),
    path("checkout/", views.checkout, name="checkout"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("form/", views.form, name="form"),
]