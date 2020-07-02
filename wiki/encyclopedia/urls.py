from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("newentry", views.newentry, name="newentry"),
    path("saveentry", views.saveentry, name="saveentry"),
    path("wiki/<str:title>/editentry", views.editentry, name="editentry"),
    path("wiki/<str:title>/saveeditentry", views.saveeditentry, name="saveeditentry"),
    path("randompage", views.randompage, name="randompage"),
    path("error", views.error, name="error")
]
