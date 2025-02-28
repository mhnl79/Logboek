from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_home_view_status_code(self):
        # Verstuur een GET-verzoek naar de URL van de 'home' view
        response = self.client.get(reverse('home'))
        # Controleer of de responsstatuscode 200 (OK) is
        self.assertEqual(response.status_code, 200)

    def test_home_template_used(self):
        # Verstuur een GET-verzoek naar de URL van de 'home' view
        response = self.client.get(reverse('home'))
        # Controleer of de 'home.html' template gebruikt wordt in de respons
        self.assertTemplateUsed(response, 'home.html')


class ContactViewTests(TestCase):
    def test_contact_view_status_code(self):
        # Verstuur een GET-verzoek naar de URL van de 'contact' view
        response = self.client.get(reverse('contact'))
        # Controleer of de responsstatuscode 200 (OK) is
        self.assertEqual(response.status_code, 200)

    def test_contact_template_used(self):
        # Verstuur een GET-verzoek naar de URL van de 'contact' view
        response = self.client.get(reverse('contact'))
        # Controleer of de 'contact.html' template gebruikt wordt in de respons
        self.assertTemplateUsed(response, 'contact.html')

