from rest_framework.test import APITestCase
from core.models import SiteSettings, Lead


class PublicApiTests(APITestCase):
    def test_health_endpoint(self):
        response = self.client.get('/api/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'ok')

    def test_site_endpoint_is_public(self):
        SiteSettings.objects.create(phone='09120000000')
        response = self.client.get('/api/site/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['site']['phone'], '09120000000')

    def test_lead_requires_core_fields(self):
        response = self.client.post('/api/leads/', {'name': '', 'phone': '', 'location': ''}, format='json')
        self.assertEqual(response.status_code, 400)

    def test_valid_lead_is_saved(self):
        payload = {
            'name': 'علی رضایی',
            'phone': '09121234567',
            'vehicle': 'پژو',
            'problem': 'battery',
            'location': 'مشهد، بلوار وکیل آباد',
            'description': 'خودرو استارت نمی خورد',
            'website': '',
        }
        response = self.client.post('/api/leads/', payload, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Lead.objects.count(), 1)
