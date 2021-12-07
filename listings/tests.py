from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import BookingInfo, ReservedInfo
import json
import urllib


class JobCreationTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.create_job_url = reverse('available_units')

    def test_case_one(self):
        # prepared data
        max_price = 50
        check_in = "2021-12-06"
        check_out = "2021-12-15"

        # make request
        url = self.create_job_url + f"?max_price={max_price}&check_in={check_in}&check_out={check_out}"
        response = self.client.get(url)
        # Check status response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check database
        self.assertEqual(len(response.json()), 1)

    def test_case_two(self):
        # prepared data
        max_price = 60
        check_in = "2021-12-06"
        check_out = "2021-12-15"

        # make request
        url = self.create_job_url + f"?max_price={max_price}&check_in={check_in}&check_out={check_out}"
        response = self.client.get(url)
        # Check status response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check database
        self.assertEqual(len(response.json()) >= 1, True)

    def test_case_three(self):
        # prepared data
        max_price = 200
        check_in = "2021-12-06"
        check_out = "2021-12-15"

        # make request
        url = self.create_job_url + f"?max_price={max_price}&check_in={check_in}&check_out={check_out}"
        response = self.client.get(url)
        # Check status response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check database
        self.assertEqual(len(response.json()), 7)
