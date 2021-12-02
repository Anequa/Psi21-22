from shelter.models import Reservation
from shelter.models import Photo
from shelter.models import Cage
from shelter.models import Animal
from shelter.models import Adoption
from authentication.models import User, Worker

# from django.shortcuts import render
# from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import AdoptionSerializer, AnimalSerializer, CageSerializer, PhotoSerializer, ReservationSerializer, UserSerializer, WorkerSerializer


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
class UserList(APIView):
    
    def get(self,request,format=None):
        users = User.objects.filter(is_staff=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# @api_view(["GET"])
# def userList(request):
    # users = User.objects.filter(is_staff=False)
    # serializer = UserSerializer(users, many=True)
    # return Response(serializer.data)


# user detail
class UserDetail(APIView):
    def get(self,request,pk,format=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response("User matching query does not exist.")

# @api_view(["GET"])
# def userDetail(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user, many=False)
#         return Response(serializer.data)
#     except User.DoesNotExist:
#         return Response("User matching query does not exist.")


# user create
class UserCreate(APIView):
    def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Update is not posible")
# @api_view(["POST"])
# def userCreate(request):
    # serializer = UserSerializer(data=request.data)

    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
    # return Response("Update is not posible")


# user update
class UserUpdate(APIView):
    def post(self,request, pk,format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response("User matching query does not exist.")

        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Update is not posible")

# @api_view(["POST"])
# def userUpdate(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response("User matching query does not exist.")

#     serializer = UserSerializer(instance=user, data=request.data)

#     # if user.email != request.data["email"]:
#     #     return serializers.ValidationError("Email field can not be changed.")
#     # nieeeeee

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response("Update is not posible")


# user filtruj
# filter dla all zmiennych

# user delete
class UserDelete(APIView):
    def delete(self,request, pk,format=None):
        try:
            User.objects.get(pk=pk).delete()
        except User.DoesNotExist:
            return Response("User matching query does not exist.")
        return Response("User succesfully deleted.")

# @api_view(["GET"])
# def userDelete(request, pk):
#     try:
#         User.objects.get(pk=pk).delete()
#     except User.DoesNotExist:
#         return Response("User matching query does not exist.")
#     return Response("User succesfully deleted.")


class WorkerList(APIView):
    def get(self,request,format=None):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)
# worker list
# @api_view(["GET"])
# def workerList(request):
#     workers = Worker.objects.all()
#     serializer = WorkerSerializer(workers, many=True)
#     return Response(serializer.data)
class WorkerDetail(APIView):
    def get(self,request,pk,format=None):
        try:
            worker = Worker.objects.get(pk=pk)
            serializer = WorkerSerializer(worker, many=False)
            return Response(serializer.data)
        except Worker.DoesNotExist:
            return Response("Worker matching query does not exist.")
# worker detail
# @api_view(["GET"])
# def workerDetail(request, pk):
#     try:
#         worker = Worker.objects.get(pk=pk)
#         serializer = WorkerSerializer(worker, many=False)
#         return Response(serializer.data)
#     except Worker.DoesNotExist:
#         return Response("Worker matching query does not exist.")

class WorkerCreate(APIView):
    def post(self,request,pk,format=None):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)
# worker create
# @api_view(["POST"])
# def workerCreate(request):
#     serializer = WorkerSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer._errors)

class WorkerUpdate(APIView):
    def post(self,request,pk,format=None):
        try:
            worker = Worker.objects.get(pk=pk)
        except Worker.DoesNotExist:
            return Response("Worker matching query does not exist.")

        serializer = WorkerSerializer(instance=worker, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)
# worker update
# @api_view(["POST"])
# def workerUpdate(request, pk):
#     try:
#         worker = Worker.objects.get(pk=pk)
#     except Worker.DoesNotExist:
#         return Response("Worker matching query does not exist.")

#     serializer = WorkerSerializer(instance=worker, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer._errors)
class WorkerDelete(APIView):
    def delete(self,request,pk,format=None):
        try:
            Worker.objects.get(pk=pk).delete()
        except Worker.DoesNotExist:
            return Response("Worker matching query does not exist.")
        return Response("Worker succesfully deleted.")


# worker delete
# @api_view(["GET"])
# def workerDelete(request, pk):
#     try:
#         Worker.objects.get(pk=pk).delete()
#     except Worker.DoesNotExist:
#         return Response("Worker matching query does not exist.")
#     return Response("Worker succesfully deleted.")

class AdoptionList(APIView):
    
    def get(self,request,format=None):
        adoptions = Adoption.objects.all()
        serializer = AdoptionSerializer(adoptions, many=True)
        return Response(serializer.data)

class AdoptionUpdate(APIView):
    def post(self,request, pk,format=None):
        try:
            adoption = Adoption.objects.get(pk=pk)
        except Adoption.DoesNotExist:
            return Response("User matching query does not exist.")

        serializer = UserSerializer(instance=adoption, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Update is not possible")



class AdoptionDetail(APIView):
    def get(self,request,pk,format=None):
        try:
            adoption = Adoption.objects.get(pk=pk)
            serializer = AdoptionSerializer(adoption, many=False)
            return Response(serializer.data)
        except Adoption.DoesNotExist:
            return Response("User matching query does not exist.")

class AdoptionDelete(APIView):
    def delete(self,request, pk,format=None):
        try:
            Adoption.objects.get(pk=pk).delete()
        except Adoption.DoesNotExist:
            return Response("User matching query does not exist.")
        return Response("User succesfully deleted.")


class AnimalList(generics.ListAPIView):
    queryset=Animal.objects.all()
    serializer_class=AnimalSerializer

class AnimalDetail(APIView):
    def get(self,request,pk,format=None):
        try:
            animal = Animal.objects.get(pk=pk)
            serializer = AnimalSerializer(animal, many=False)
            return Response(serializer.data)
        except Animal.DoesNotExist:
            return Response("Animals matching query does not exist.")

class AnimalCreate(APIView):
    def post(self,request,pk,format=None):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

class AnimalUpdate(APIView):
    def post(self,request,pk,format=None):
        try:
            animal = Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            return Response("Animals matching query does not exist.")

        serializer = AnimalSerializer(instance=animal, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

class AnimalDelete(APIView):
    def delete(self,request,pk,format=None):
        try:
            Animal.objects.get(pk=pk).delete()
        except Animal.DoesNotExist:
            return Response("Animals matching query does not exist.")
        return Response("Animals succesfully deleted.")

class CagesList(generics.ListAPIView):
    queryset=Cage.objects.all()
    serializer_class=CageSerializer

class CagesDetail(APIView):
    def get(self,request,pk,format=None):
        try:
            cage = Cage.objects.get(pk=pk)
            serializer = CageSerializer(cage, many=False)
            return Response(serializer.data)
        except Cage.DoesNotExist:
            return Response("Animals matching query does not exist.")

class CagesCreate(APIView):
    def post(self,request,pk,format=None):
        serializer = CageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

class CagesUpdate(APIView):
    def post(self,request,pk,format=None):
        try:
            cage = Cage.objects.get(pk=pk)
        except Cage.DoesNotExist:
            return Response("Cagess matching query does not exist.")

        serializer = CageSerializer(instance=cage, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

class CagesDelete(APIView):
    def delete(self,request,pk,format=None):
        try:
            Cage.objects.get(pk=pk).delete()
        except Cage.DoesNotExist:
            return Response("Cagess matching query does not exist.")
        return Response("Cagess succesfully deleted.")

class PhotoList(generics.ListAPIView):
    queryset=Photo.objects.all()
    serializer_class=PhotoSerializer

class PhotoDetail(APIView):
    def get(self,request,pk,format=None):
        try:
            photo = Photo.objects.get(pk=pk)
            serializer = PhotoSerializer(photo, many=False)
            return Response(serializer.data)
        except Photo.DoesNotExist:
            return Response("Photo matching query does not exist.")

class PhotoCreate(APIView):
    def post(self,request,pk,format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

class PhotoUpdate(APIView):
    def post(self,request,pk,format=None):
        try:
            photo = Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            return Response("Photo matching query does not exist.")

        serializer = PhotoSerializer(instance=photo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

class PhotoDelete(APIView):
    def delete(self,request,pk,format=None):
        try:
            Photo.objects.get(pk=pk).delete()
        except Photo.DoesNotExist:
            return Response("Photo matching query does not exist.")
        return Response("Photo succesfully deleted.")

class ReservationsList(generics.ListAPIView):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

class ReservationsDetail(APIView):
    def get(self,request,pk,format=None):
        try:
            reservation = Reservation.objects.get(pk=pk)
            serializer = ReservationSerializer(reservation, many=False)
            return Response(serializer.data)
        except Reservation.DoesNotExist:
            return Response("Reservations matching query does not exist.")

class ReservationsCreate(APIView):
    def post(self,request,pk,format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

class ReservationsUpdate(APIView):
    def post(self,request,pk,format=None):
        try:
            reservation = Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return Response("Reservations matching query does not exist.")

        serializer = PhotoSerializer(instance=reservation, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

class ReservationsDelete(APIView):
    def delete(self,request,pk,format=None):
        try:
            Reservation.objects.get(pk=pk).delete()
        except Reservation.DoesNotExist:
            return Response("Reservations matching query does not exist.")
        return Response("Reservations succesfully deleted.")