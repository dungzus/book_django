from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("getall/", view=views.getAll, name="all"),
    path("<int:book_id>/", view=views.getDetail, name="detail"),
]
