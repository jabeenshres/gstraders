from django.urls import path
from extras.views import (
    HeroPageAddView,
    HeroPageListView,
    HeroPageUpdateView,
    HeroPageDeleteView,
    ContactMessage,
    ContactListView
)

app_name = "extras"

urlpatterns = [
    path("create/", HeroPageAddView.as_view(), name='hero-page-create'),
    path("list/", HeroPageListView.as_view(), name='hero-page-list'),
    path("update/<int:pk>/", HeroPageUpdateView.as_view(), name='hero-page-update'),
    path("delete/<int:pk>/", HeroPageDeleteView.as_view(), name='hero-page-delete'),


    path("contact/us/", ContactMessage.as_view(), name='contact-us'),
    path("contact/us/list/", ContactListView.as_view(), name='contact-us-list'),
    

]