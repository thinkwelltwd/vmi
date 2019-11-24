from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class GenerateReportTest(TestCase):
    # Includes two orgs, ACME Health and Transparent Health
    fixtures = ['sample-test-orgs']

    def setUp(self):
        self.client = Client()
        self.url = reverse('orgs_and_agents_report')
        self.client.login(username="poc", password="pocpassword")

    def test_report_generation(self):
        """
        test_report_generation
        """
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
