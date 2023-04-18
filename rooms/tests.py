# from django.test import TestCase
from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestAmenities(APITestCase):
    # def test_two_plus_two(self):
    #     self.assertEqual(2 + 2, 5, "the math is wrong.")
    URL = "/api/v1/rooms/amenities/"
    NAME = "Amenity test"
    DESCRIPTION = "description"

    def setUp(self) -> None:
        models.Amenity.objects.create(name=self.NAME, description=self.DESCRIPTION)

    def test_all_amenities(self):
        res = self.client.get(self.URL)
        data = res.json()
        self.assertEqual(res.status_code, 200, "status code isn't 200.")
        self.assertIsInstance(data, list, "not list")
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.NAME, "not equal name")
        self.assertEqual(
            data[0]["description"], self.DESCRIPTION, "not equal description"
        )

    def test_create_amenity(self):
        NAME = "create test"
        DESCRIPTION = "create test description"
        res = self.client.post(
            self.URL, data={"name": NAME, "description": DESCRIPTION}
        )
        data = res.json()
        self.assertEqual(res.status_code, 200, "not 200 status code")
        self.assertEqual(data["name"], NAME, "name not equal")
        self.assertEqual(data["description"], DESCRIPTION, "description not equal")

        res = self.client.post(self.URL, data={"description": DESCRIPTION})
        data = res.json()
        self.assertEqual(res.status_code, 400)
        self.assertIn("name", data)


class TestAmenity(APITestCase):
    NAME = "TEST"
    DESCRIPTION = "TEST DESC."
    URL_PREFIX = "/api/v1/rooms/amenities/"

    def setUp(self) -> None:
        models.Amenity.objects.create(name=self.NAME, description=self.DESCRIPTION)

    def test_amenity_not_found(self):
        res = self.client.get(f"{self.URL_PREFIX}2")
        self.assertEqual(res.status_code, 404)

    def test_get_amenity(self):
        res = self.client.get(f"{self.URL_PREFIX}1")
        self.assertEqual(res.status_code, 200)

        data = res.json()
        self.assertEqual(data["name"], self.NAME)
        self.assertEqual(data["description"], self.DESCRIPTION)

    def test_put_amenity(self):
        res = self.client.put(
            f"{self.URL_PREFIX}1",
            data={"name": self.NAME, "description": self.DESCRIPTION},
        )
        data = res.json()
        self.assertEqual(res.status_code, 200, "status code not 200")
        self.assertEqual(data["name"], self.NAME, "name not equal")
        self.assertEqual(data["description"], self.DESCRIPTION, "name not equal")

        res = self.client.put(
            f"{self.URL_PREFIX}1",
            data={
                "name": "akjwhlefhalksjdhflakjhlewksjhflakjhwlfekjhalsdhjflajuehjahslkdjhbflakjhleuwhlakjshdlkjfahlskjdhflkjahluewhflakjshldjkfhalskjdhflkajhwleuihfa;owsh;ajkxcn;vm,zxnclvknmbalkjhwe3fuiahwelfjhlaskjdlvkxbckvnmzblc"
            },
        )
        data = res.json()
        self.assertEqual(res.status_code, 400, "status code not 404")
        self.assertIn("name", data, "return data is wrong.")

    def test_delete_amenity(self):
        res = self.client.delete(f"{self.URL_PREFIX}1")
        self.assertEqual(res.status_code, 204)


class TestRoom(APITestCase):
    URL = "/api/v1/rooms/"

    def setUp(self) -> None:
        user = User.objects.create(username="test")
        user.set_password("123")
        user.save()
        self.user = user

    def test_create_room(self):
        res = self.client.post(self.URL)
        self.assertEqual(res.status_code, 403)

        # self.client.login(username="test", password="123")
        self.client.force_login(self.user)

        res = self.client.post(self.URL)
        self.assertEqual(res.status_code, 400)
