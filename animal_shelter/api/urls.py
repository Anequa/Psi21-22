from django.urls import path

from . import views

urlpatterns = [
    path("", views.RootApi.as_view(), name=views.RootApi.name),
    path("user/list/", views.UserList.as_view(), name=views.UserList.name),
    path(
        "user/detail/<str:pk>/", views.UserDetail.as_view(), name=views.UserDetail.name
    ),
    path("worker/list/", views.WorkerList.as_view(), name=views.WorkerList.name),
    path(
        "worker/detail/<str:pk>/",
        views.WorkerDetail.as_view(),
        name=views.WorkerDetail.name,
    ),
    path("adoption/list/", views.AdoptionList.as_view(), name=views.AdoptionList.name),
    path(
        "adoption/detail/<str:pk>/",
        views.AdoptionDetail.as_view(),
        name=views.AdoptionDetail.name,
    ),
    path(
        "reservation/list/",
        views.ReservationList.as_view(),
        name=views.ReservationList.name,
    ),
    path(
        "reservation/detail/<str:pk>/",
        views.ReservationDetail.as_view(),
        name=views.ReservationDetail.name,
    ),
    path(
        "photo/list/",
        views.PhotoList.as_view(),
        name=views.PhotoList.name,
    ),
    path(
        "photo/detail/<str:pk>/",
        views.PhotoDetail.as_view(),
        name=views.PhotoDetail.name,
    ),
    path(
        "cage/list/",
        views.CageList.as_view(),
        name=views.CageList.name,
    ),
    path(
        "cage/detail/<str:pk>/",
        views.CageDetail.as_view(),
        name=views.CageDetail.name,
    ),
    path(
        "animal/list/",
        views.AnimalList.as_view(),
        name=views.AnimalList.name,
    ),
    path(
        "animal/detail/<str:pk>/",
        views.AnimalDetail.as_view(),
        name=views.AnimalDetail.name,
    ),
]
