from django.test import TestCase, Client
from company.models import Company
from django.utils.text import slugify
from django.shortcuts import  reverse
from django.utils.text import slugify
from .validators import  date_in_future_validator , digits_only_validators
class CompanyFormTest(TestCase):
    """ Wir erstellen via Formular Absenden ein Testobjekt in der DB,
    und prüfen dieses dann.

    Unit-Test Schritte:
    1) Test-Objekt/Test-Daten anlegen
    2) Aktion durchführen, zb. Formular absenden

    self.assertTrue(True)
    self.assertEqual("a", "a")
    self.assertNotEqual("a", "b")

    """
    def setUp(self):
        self.client = Client()  # der User, das Formular abschickt
        self.payload = {
            "name": "Mc Donalds GmbH",
            "description": "bla bla bla",
            "company_type": "food",
            "has_restaurants": True,
            "slogan": "das ist der slogan"
        }
    
    
       
    def test_company_has_proper_slug(self):
        """prüfe, ob nach Absenden des Formulars das Objekt 
        mit dem richtigen Slug angelegt wurde (klein, keine Leerzeichen)
        """
        
        # Formular absenden:
        self.client.post(reverse("company:company_add"), self.payload)
        company = Company.objects.get(name=self.payload.get("name"))

        self.assertEqual(company.slug, "mc-donalds-gmbh")
        self.assertEqual(company.slug, slugify(self.payload.get("name")))

    def test_company_type_is_food_and_has_restaurant(self):
        """Prüfen, ob eine Firma vom Typ food UND zugleich has_restaurant True 
        ist"""
        self.client.post(reverse("company:company_add"), self.payload)
        company_exist = Company.objects.filter(
            name=self.payload.get("name")).exists()

        # Objekt muss eingetragen sein, weil food und Restaurant erlaubt ist
        self.assertTrue(company_exist)

    def test_company_type_is_tech_and_has_restaurant(self):
        """Prüfen, ob eine Firma vom Typ tech UND zugleich has_restaurant True 
        ist"""
        self.payload["company_type"] = "tech"
        self.client.post(reverse("company:company_add"), self.payload)
        company_exist = Company.objects.filter(
            name=self.payload.get("name")).exists()

        # Objekt darf nicht eingetragen sein,
        # weil company_type=tech und Restaurant NICHT erlaubt sind
        self.assertFalse(company_exist)





    def test_create_companies_with_same_name(self):
        self.client.post(reverse("company:company_add"), self.payload)
        self.client.post(reverse("company:company_add"), self.payload)
        companies = Company.objects.filter(name=self.payload.get("name"))
        self.assertEqual(len(companies),1)