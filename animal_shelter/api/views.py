from authentication.models import User, Worker
from django_filters import DateFilter, FilterSet, NumberFilter
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from shelter.models import Adoption, Animal, Cage, Photo, Reservation

from .serializers import (
    AdoptionSerializer,
    AnimalSerializer,
    CageSerializer,
    PhotoSerializer,
    ReservationSerializer,
    UserSerializer,
    UserSerializerWhenUpdate,
    WorkerSerializer,
    WorkerSerializerWhenUpdate,
)


class RootApi(generics.GenericAPIView):
    name = "root-api"

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Response(
                {
                    "user": reverse(UserList.name, request=request),
                    "worker": reverse(WorkerList.name, request=request),
                    "adoption": reverse(AdoptionList.name, request=request),
                    "reservation": reverse(ReservationList.name, request=request),
                    "photo": reverse(PhotoList.name, request=request),
                    "cage": reverse(CageList.name, request=request),
                    "animal": reverse(AnimalList.name, request=request),
                }
            )
        else:
            return Response(
                {
                    "adoption": reverse(AdoptionList.name, request=request),
                    "reservation": reverse(ReservationList.name, request=request),
                    "photo": reverse(PhotoList.name, request=request),
                    "cage": reverse(CageList.name, request=request),
                    "animal": reverse(AnimalList.name, request=request),
                }
            )


# user
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    name = "user-list"
    ordering_fields = [
        "pk",
        "first_name",
        "last_name",
        "email",
        "phone",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "phone",
    ]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializerWhenUpdate
    name = "user-detail"


class WorkerList(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    name = "worker-list"
    ordering_fields = [
        "pk",
        "first_name",
        "last_name",
        "email",
        "phone",
        "wage",
    ]
    search_fields = ["first_name", "last_name", "email", "phone"]


class WorkerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializerWhenUpdate
    name = "worker-detail"


# Adoption
class AdoptionFilter(FilterSet):
    from_create_date = DateFilter(field_name="create_date", lookup_expr="gte")
    to_create_date = DateFilter(field_name="create_date", lookup_expr="lte")
    from_adoption_date = DateFilter(field_name="adoption_date", lookup_expr="gte")
    to_adoption_date = DateFilter(field_name="adoption_date", lookup_expr="lte")

    class Meta:
        model = Adoption
        fields = [
            "agreement",
            "status",
            "user",
            "animal",
            "from_create_date",
            "to_create_date",
            "from_adoption_date",
            "to_adoption_date",
        ]


class AdoptionList(generics.ListCreateAPIView):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer
    name = "adoption-list"
    filter_class = AdoptionFilter
    ordering_fields = ["pk", "adoption_date", "create_date"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdoptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer
    name = "adoption-detail"


# reservation
class ReservationFilter(FilterSet):
    from_create_date = DateFilter(field_name="create_date", lookup_expr="gte")
    to_create_date = DateFilter(field_name="create_date", lookup_expr="lte")
    from_reservation_date = DateFilter(field_name="reservation_date", lookup_expr="gte")
    to_reservation_date = DateFilter(field_name="reservation_date", lookup_expr="lte")

    class Meta:
        model = Reservation
        fields = [
            "user",
            "animal",
            "from_create_date",
            "to_create_date",
            "from_reservation_date",
            "to_reservation_date",
        ]


class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    name = "reservation-list"
    filter_class = ReservationFilter
    ordering_fields = ["pk", "reservation_date"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    name = "reservation-detail"


# photo
class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    name = "photo-list"
    filter_fields = ["animal"]
    ordering_fields = ["pk"]
    search_fields = ["alter"]


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    name = "photo-detail"


# cage
class CageFilter(FilterSet):
    from_space = NumberFilter(field_name="space", lookup_expr="gte")
    to_space = NumberFilter(field_name="space", lookup_expr="lte")
    from_cage_number = NumberFilter(field_name="cage_number", lookup_expr="gte")
    to_cage_number = NumberFilter(field_name="cage_number", lookup_expr="lte")

    class Meta:
        model = Cage
        fields = [
            "species",
            "section",
            "space",
            "from_space",
            "to_space",
            "from_cage_number",
            "to_cage_number",
        ]


class CageList(generics.ListCreateAPIView):
    queryset = Cage.objects.all()
    serializer_class = CageSerializer
    name = "cage-list"
    filter_class = CageFilter
    ordering_fields = ["pk", "cage_number", "section", "space"]
    search_fields = ["alter", "cage_identificator", "cage_number", "space"]


class CageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cage.objects.all()
    serializer_class = CageSerializer
    name = "cage-detail"


# animal
class AnimalFilter(FilterSet):
    from_age = NumberFilter(field_name="age", lookup_expr="gte")
    to_age = NumberFilter(field_name="age", lookup_expr="lte")

    class Meta:
        model = Animal
        fields = ["species", "gender", "size", "status", "cage", "from_age", "to_age"]


class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    name = "animal-list"
    filter_class = AnimalFilter
    ordering_fields = [
        "pk",
        "species",
        "gender",
        "size",
        "status",
        "cage",
        "name",
        "age",
        "date_of_arrival",
        "estimate_year_of_birth",
    ]
    search_fields = ["name", "description", "status", "species", "gender"]


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    name = "animal-detail"
