from rest_framework import status
from rest_framework.test import APITestCase


class APITests(APITestCase):

    def test_get_visited_domains_check_status_code_200(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/visited_domains/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_visited_domains_check_content_type_json(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/visited_domains/'
        )
        self.assertEqual(response.headers["Content-Type"], 'application/json')

    def test_get_visited_domains_check_fields(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/visited_domains/'
        )
        fields = list(iter(response.json().keys()))
        self.assertEqual(fields, ['domains', 'status'])
