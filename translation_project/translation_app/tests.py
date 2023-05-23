# 3rd party library import
import pytest
# Django import 
from django.urls import reverse
# Third party rest_framework import
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
class TestTranslationAPI:

    @pytest.fixture
    def api_client(self):
        return APIClient()

    def test_translation(self, api_client):
        url = reverse('translate_text')
        params = {
            'text': 'Hello',
            'target_language': 'fr',
            'source_language': 'en',
        }
        response = api_client.get(url, params)
        assert response.status_code == status.HTTP_200_OK
        assert 'translation' in response.data
        assert response.data['translation'] == 'Bonjour'
