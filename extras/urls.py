from django.urls import path
from extras.views import (
    HeroPageAddView,
    HeroPageListView,
    HeroPageUpdateView,
    HeroPageDeleteView
)

app_name = "extras"

urlpatterns = [
    path("create/", HeroPageAddView.as_view(), name='hero-page-create'),
    path("list/", HeroPageListView.as_view(), name='hero-page-list'),
    path("update/<int:pk>/", HeroPageUpdateView.as_view(), name='hero-page-update'),
    path("delete/<int:pk>/", HeroPageDeleteView.as_view(), name='hero-page-delete'),
]