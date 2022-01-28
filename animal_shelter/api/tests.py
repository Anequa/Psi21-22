from authentication.models import Worker
from django import urls
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase
from shelter.models import Cage

from . import views


def _login(username, email, password):
    Worker.objects.create_superuser(username=username, email=email, password=password)
    client = APIClient()
    client.login(username=username, password=password)
    return client


class CageTests(APITestCase):
    def post_cage(self, cage_nr, section, space, species, client):
        url = reverse(views.CageList.name)
        data = {
            "cage_number": cage_nr,
            "space": space,
            "section": section,
            "species": species,
        }
        response = client.post(url, data, format="json")
        return response

    def test_post_and_get_cage(self):
        client = _login("admin", "admin@admin.com", "admin123")
        new_cage_nr = 1
        new_cage_space = 3
        new_cage_section = "A"
        new_cage_species = "Dog"
        response = self.post_cage(
            new_cage_nr, new_cage_section, new_cage_space, new_cage_species, client
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cage.objects.count(), 1)
        assert Cage.objects.get().cage_number == new_cage_nr
        assert Cage.objects.get().section == new_cage_section
        assert Cage.objects.get().space == new_cage_space
        assert Cage.objects.get().species == new_cage_species

    def test_post_existing_cage(self):
        client = _login("admin", "admin@admin.com", "admin123")
        new_cage_nr = 1
        new_cage_space = 3
        new_cage_section = "A"
        new_cage_species = "Dog"

        response_one = self.post_cage(
            new_cage_nr, new_cage_section, new_cage_space, new_cage_species, client
        )
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_cage(
            new_cage_nr, new_cage_section, new_cage_space, new_cage_species, client
        )
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_cage_by_species(self):
        client = _login("admin", "admin@admin.com", "admin123")
        cage_nr = 1
        cage_space = 3
        cage_section = "A"
        cage_species = "Dog"

        cage_nr2 = 1
        cage_space2 = 2
        cage_section2 = "B"
        cage_species2 = "Cat"

        self.post_cage(cage_nr, cage_section, cage_space, cage_species, client)

        self.post_cage(cage_nr2, cage_section2, cage_space2, cage_species2, client)

        filter_by_species = {"species": cage_species}
        url = "{0}?{1}".format(
            reverse(views.CageList.name), urlencode(filter_by_species)
        )
        response = client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
        assert response.data["results"][0]["cage_number"] == cage_nr
        assert response.data["results"][0]["species"] == cage_species
        assert response.data["results"][0]["space"] == cage_space
        assert response.data["results"][0]["section"] == cage_section

    def test_get_cage_collection(self):
        client = _login("admin", "admin@admin.com", "admin123")
        cage_nr = 1
        cage_space = 3
        cage_section = "A"
        cage_species = "Dog"

        cage_nr2 = 1
        cage_space2 = 2
        cage_section2 = "B"
        cage_species2 = "Cat"

        self.post_cage(cage_nr, cage_section, cage_space, cage_species, client)

        self.post_cage(cage_nr2, cage_section2, cage_space2, cage_species2, client)

        url = reverse(views.CageList.name)
        response = client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 2
        assert response.data["results"][0]["cage_number"] == cage_nr
        assert response.data["results"][0]["species"] == cage_species
        assert response.data["results"][0]["space"] == cage_space
        assert response.data["results"][0]["section"] == cage_section
        assert response.data["results"][1]["cage_number"] == cage_nr2
        assert response.data["results"][1]["species"] == cage_species2
        assert response.data["results"][1]["space"] == cage_space2
        assert response.data["results"][1]["section"] == cage_section2

    def test_update_cage(self):
        client = _login("admin", "admin@admin.com", "admin123")
        cage_nr = 1
        cage_space = 3
        cage_section = "A"
        cage_species = "Dog"

        response = self.post_cage(
            cage_nr, cage_section, cage_space, cage_species, client
        )

        url = urls.reverse(views.CageDetail.name, None, {response.data["pk"]})
        update_cage_species = "Cat"
        data = {
            "cage_number": cage_nr,
            "space": cage_space,
            "section": cage_section,
            "species": update_cage_species,
        }
        patch_response = client.patch(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert patch_response.data["species"] == update_cage_species

    def test_update_existing_cage(self):
        client = _login("admin", "admin@admin.com", "admin123")
        new_cage_nr = 1
        new_cage_space = 3
        new_cage_section = "A"
        new_cage_species = "Dog"

        new_cage_nr2 = 2
        new_cage_space2 = 3
        new_cage_section2 = "A"
        new_cage_species2 = "Dog"

        response_one = self.post_cage(
            new_cage_nr, new_cage_section, new_cage_space, new_cage_species, client
        )

        response_two = self.post_cage(
            new_cage_nr2, new_cage_section2, new_cage_space2, new_cage_species2, client
        )

        assert response_one.status_code == status.HTTP_201_CREATED
        assert response_two.status_code == status.HTTP_201_CREATED

        update_cage_nr2 = 1

        update_response = self.post_cage(
            update_cage_nr2,
            new_cage_section2,
            new_cage_space2,
            new_cage_species2,
            client,
        )

        assert update_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_cage(self):
        client = _login("admin", "admin@admin.com", "admin123")
        cage_nr = 1
        cage_space = 3
        cage_section = "A"
        cage_species = "Dog"

        response = self.post_cage(
            cage_nr, cage_section, cage_space, cage_species, client
        )

        url = urls.reverse(views.CageDetail.name, None, {response.data["pk"]})
        get_response = client.patch(url, format="json")

        assert get_response.status_code == status.HTTP_200_OK
        assert response.data["cage_number"] == cage_nr
        assert response.data["species"] == cage_species
        assert response.data["space"] == cage_space
        assert response.data["section"] == cage_section

class WorkerTest(APITestCase):
    def create_worker(
        self,
        password,
        username,
        email,
        first_name,
        last_name,
        phone,
        city,
        zip_code,
        address_line1,
        address_line2,
        bank_account_number,
        wage,
        is_superuser,
        is_staff,
        client,
    ):
        url = reverse(views.WorkerList.name)
        data = {
            "password": password,
            "username": username,
            "email": email,
            "first_name": first_name,
            "phone": phone,
            "last_name": last_name,
            "city": city,
            "zip_code": zip_code,
            "address_line1": address_line1,
            "address_line2": address_line2,
            "bank_account_number": bank_account_number,
            "wage": wage,
            "bank_account_number": bank_account_number,
            "wage": wage,
            "is_superuser": is_superuser,
            "is_staff": is_staff,
        }
        response = client.post(url, data, format="json")
        return response

    def test_post_and_get_worker(self):
        client = _login("admin", "admin@admin.com", "admin123")
        password = "worker24"
        username = "worker1"
        email = "worker1@us.com"
        first_name = "Adam"
        last_name = "Pola"
        phone = "500050122"
        city = "Olsztyn"
        zip_code = "12-123"
        address_line1 = "Polna 23"
        address_line2 = ""
        bank_account_number = 12121212123434343434567890
        wage = 2000
        is_superuser = False
        is_staff = True

        response = self.create_worker(
            password,
            username,
            email,
            first_name,
            last_name,
            phone,
            city,
            zip_code,
            address_line1,
            address_line2,
            bank_account_number,
            wage,
            is_superuser,
            is_staff,
            client,
        )
        worker = APIClient()
        isLogged = worker.login(username="worker1", password="worker24")

        assert response.status_code == status.HTTP_201_CREATED
        assert Worker.objects.filter(is_superuser=False).count() == 1
        assert Worker.objects.filter(is_superuser=True).count() == 1
        assert Worker.objects.filter(is_superuser=False).get().first_name == "Adam"
        assert Worker.objects.filter(is_superuser=False).get().last_name == "Pola"
        assert isLogged
