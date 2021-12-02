from django.urls import path

# from shelter.views import HomePageView
from . import views

urlpatterns = [
    # path("", HomePageView.as_view(), name="home_page"),
    path("", views.apiOverview, name="api-overview"),
    path("user/list/", views.UserList.as_view(), name="user-list"),
    path("user/create/", views.UserCreate.as_view(), name="user-create"),
    path("user/update/<str:pk>/", views.UserUpdate.as_view(), name="user-update"),
    path("user/delete/<str:pk>/", views.UserDelete.as_view(), name="user-delete"),
    path("user/detail/<str:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("worker/list/", views.WorkerList.as_view(), name="worker-list"),
    path("worker/create/", views.WorkerCreate.as_view(), name="worker-create"),
    path("worker/update/<str:pk>/", views.WorkerUpdate.as_view(), name="worker-update"),
    path("worker/delete/<str:pk>/", views.WorkerDelete.as_view(), name="worker-delete"),
    path("worker/detail/<str:pk>/", views.WorkerDetail.as_view(), name="worker-detail"),
    path("adoption/list/", views.AdoptionList.as_view(), name="adoption-list"),
    path("adoption/update/<str:pk>/", views.AdoptionUpdate.as_view(), name="adoption-update"),
    path("adoption/detail/<str:pk>/", views.AdoptionDetail.as_view(), name="adoption-detail"),
    path("adoption/delete/<str:pk>/", views.AdoptionDelete.as_view(), name="adoption-delete"),
    path("animals/list/", views.AnimalList.as_view(), name="animal-list"),
    path("animals/create/", views.AnimalCreate.as_view(), name="animal-create"),
    path("animals/update/<str:pk>/", views.AnimalUpdate.as_view(), name="cage-update"),
    path("animals/delete/<str:pk>/", views.AnimalDelete.as_view(), name="cage-delete"),
    path("animals/detail/<str:pk>/", views.AnimalDetail.as_view(), name="cage-detail"),
    path("cages/list/", views.CagesList.as_view(), name="cage-list"),
    path("cages/create/", views.CagesCreate.as_view(), name="cage-create"),
    path("cages/update/<str:pk>/", views.CagesUpdate.as_view(), name="cage-update"),
    path("cages/delete/<str:pk>/", views.CagesDelete.as_view(), name="cage-delete"),
    path("cages/detail/<str:pk>/", views.CagesDetail.as_view(), name="cage-detail"),
    path("photos/list/", views.PhotoList.as_view(), name="photo-list"),
    path("photos/create/", views.PhotoCreate.as_view(), name="photo-create"),
    path("photos/update/<str:pk>/", views.PhotoUpdate.as_view(), name="photo-update"),
    path("photos/delete/<str:pk>/", views.PhotoDelete.as_view(), name="photo-delete"),
    path("photos/detail/<str:pk>/", views.PhotoDetail.as_view(), name="photo-detail"),
    path("reservations/list/", views.ReservationsList.as_view(), name="reservation-list"),
    path("reservations/create/", views.ReservationsCreate.as_view(), name="reservation-create"),
    path("reservations/update/<str:pk>/", views.ReservationsUpdate.as_view(), name="reservation-update"),
    path("reservations/delete/<str:pk>/", views.ReservationsDelete.as_view(), name="reservation-delete"),
    path("reservations/detail/<str:pk>/", views.ReservationsDetail.as_view(), name="reservation-detail"),
    
]
