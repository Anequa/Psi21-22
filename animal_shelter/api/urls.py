from django.urls import path

# from shelter.views import HomePageView
from . import views

urlpatterns = [
    # path("", HomePageView.as_view(), name="home_page"),
    path("", views.apiOverview, name="api-overview"),
    path("user/list/", views.userList, name="user-list"),
    path("user/create/", views.userCreate, name="user-create"),
    path("user/update/<str:pk>/", views.userUpdate, name="user-update"),
    path("user/delete/<str:pk>/", views.userDelete, name="user-delete"),
    path("user/detail/<str:pk>/", views.userDetail, name="user-detail"),
    path("worker/list/", views.workerList, name="worker-list"),
    path("worker/create/", views.workerCreate, name="worker-create"),
    path("worker/update/<str:pk>/", views.workerUpdate, name="worker-update"),
    path("worker/delete/<str:pk>/", views.workerDelete, name="worker-delete"),
    path("worker/detail/<str:pk>/", views.workerDetail, name="worker-detail"),
]
