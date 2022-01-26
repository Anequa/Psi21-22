from authentication.models import Worker
from django import urls
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase
from shelter.models import Cage

from . import views


class CageTests(APITestCase):
    def _login(self, username, email, password):
        Worker.objects.create_superuser(
            username=username, email=email, password=password
        )
        client = APIClient()
        client.login(username=username, password=password)
        return client

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
        client = self._login("admin", "admin@admin.com", "admin123")
        new_cage_nr = 1
        new_cage_space = 3
        new_cage_section = "A"
        new_cage_species = "Dog"
        response = self.post_cage(
            new_cage_nr, new_cage_section, new_cage_space, new_cage_species, client
        )
        # print("PK {0}".format(Cage.objects.get().pk))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cage.objects.count(), 1)
        assert Cage.objects.get().cage_number == new_cage_nr
        assert Cage.objects.get().section == new_cage_section
        assert Cage.objects.get().space == new_cage_space
        assert Cage.objects.get().species == new_cage_species

    def test_post_existing_cage(self):
        client = self._login("admin", "admin@admin.com", "admin123")
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
        # print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_cage_by_species(self):
        client = self._login("admin", "admin@admin.com", "admin123")
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
        # print(url)
        response = client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
        assert response.data["results"][0]["cage_number"] == cage_nr
        assert response.data["results"][0]["species"] == cage_species
        assert response.data["results"][0]["space"] == cage_space
        assert response.data["results"][0]["section"] == cage_section

    def test_get_cage_collection(self):
        client = self._login("admin", "admin@admin.com", "admin123")
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
        client = self._login("admin", "admin@admin.com", "admin123")
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
        # print(patch_response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert patch_response.data["species"] == update_cage_species

    def test_update_existing_cage(self):
        client = self._login("admin", "admin@admin.com", "admin123")
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

        # print(update_response)
        assert update_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_cage(self):
        client = self._login("admin", "admin@admin.com", "admin123")
        cage_nr = 1
        cage_space = 3
        cage_section = "A"
        cage_species = "Dog"

        response = self.post_cage(
            cage_nr, cage_section, cage_space, cage_species, client
        )

        url = urls.reverse(views.CageDetail.name, None, {response.data["pk"]})
        get_response = client.patch(url, format="json")
        # print(response.data)
        assert get_response.status_code == status.HTTP_200_OK
        assert response.data["cage_number"] == cage_nr
        assert response.data["species"] == cage_species
        assert response.data["space"] == cage_space
        assert response.data["section"] == cage_section
