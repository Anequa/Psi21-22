from authentication.models import User, Worker

# from django.shortcuts import render
# from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, WorkerSerializer


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "UserLista": "/user/list/",
        "UserDetail View": "/user/detail/<str:pk>/",
        "UserCreate": "/user/create/",
        "UserUpdate": "/user/update/<str:pk>/",
        "UserDelete": "/user/delete/<str:pk>/",
        "WorkerLista": "/worker/list/",
        "WorkerDetail View": "/worker/detail/<str:pk>/",
        "WorkerCreate": "/worker/create/",
        "WorkerUpdate": "/worker/update/<str:pk>/",
        "WorkerDelete": "/worker/delete/<str:pk>/",
    }
    return Response(api_urls)


# user list
@api_view(["GET"])
def userList(request):
    users = User.objects.filter(is_staff=False)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# user detail
@api_view(["GET"])
def userDetail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response("User matching query does not exist.")


# user create
@api_view(["POST"])
def userCreate(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("Update is not posible")


# user update
@api_view(["POST"])
def userUpdate(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response("User matching query does not exist.")

    serializer = UserSerializer(instance=user, data=request.data)

    # if user.email != request.data["email"]:
    #     return serializers.ValidationError("Email field can not be changed.")
    # nieeeeee

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("Update is not posible")


# user filtruj
# filter dla all zmiennych

# user delete
@api_view(["GET"])
def userDelete(request, pk):
    try:
        User.objects.get(pk=pk).delete()
    except User.DoesNotExist:
        return Response("User matching query does not exist.")
    return Response("User succesfully deleted.")


# worker list
@api_view(["GET"])
def workerList(request):
    workers = Worker.objects.all()
    serializer = WorkerSerializer(workers, many=True)
    return Response(serializer.data)


# worker detail
@api_view(["GET"])
def workerDetail(request, pk):
    try:
        worker = Worker.objects.get(pk=pk)
        serializer = WorkerSerializer(worker, many=False)
        return Response(serializer.data)
    except Worker.DoesNotExist:
        return Response("Worker matching query does not exist.")


# worker create
@api_view(["POST"])
def workerCreate(request):
    serializer = WorkerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer._errors)


# worker update
@api_view(["POST"])
def workerUpdate(request, pk):
    try:
        worker = Worker.objects.get(pk=pk)
    except Worker.DoesNotExist:
        return Response("Worker matching query does not exist.")

    serializer = WorkerSerializer(instance=worker, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer._errors)


# worker delete
@api_view(["GET"])
def workerDelete(request, pk):
    try:
        Worker.objects.get(pk=pk).delete()
    except Worker.DoesNotExist:
        return Response("Worker matching query does not exist.")
    return Response("Worker succesfully deleted.")
