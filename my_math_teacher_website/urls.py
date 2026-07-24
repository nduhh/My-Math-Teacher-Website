from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("screenshots/", views.screenshots, name="screenshots"),
    path("features/", views.features, name="features"),
    path("how-it-works/", views.how_it_works, name="how_it_works"),
    path("roadmap/", views.roadmap, name="roadmap"),
    path("contact/", views.contact, name="contact"),
    path("join-waiting-list/", views.join_waiting_list, name="join_waiting_list"),
]