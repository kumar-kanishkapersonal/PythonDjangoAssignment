from django.test import TestCase
import csv
import mock
from mock import patch
from .models import DrugReview, PharmaSales
from .serializers import DrugReviewSerializer, DrugReview


class TestCases(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ to upload data from csv to db. """
        with open("test_data\\DrugReview.csv", errors="ignore") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            sales_list = []
            for row in enumerate(reader):
                (_id, condition, date, drugName, rating, review, uniqueId, usefulCount) = row[1]
                sales_list.append(DrugReview(_id, condition, date, drugName, rating, review, uniqueId, usefulCount))
        DrugReview.objects.bulk_create(sales_list)
        with open("test_data\\PharmaSales.csv", errors="ignore") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            sales_list = []
            for row in enumerate(reader):
                (_id, date, m01ab, m01ae, n02ba, n02be, n05b, n05c, r03, r06, year) = row[1]
                sales_list.append(PharmaSales(_id, date, m01ab, m01ae, n02ba, n02be, n05b, n05c, r03, r06, year))
        PharmaSales.objects.bulk_create(sales_list)


    def test_Retrieve_Sales_by_Drug_Classification(self):
        response = self.client.post("/sales_and_reviews/Retrieve_Sales_by_Drug_Classification/",
                                    {"year": "2016",
                                    "drug_classification": "R"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["year - 2016"], 2137.0)
        self.assertEqual(response.data[0]["year - 2015"], 1721.25)
        self.assertEqual(response.data[1]["year - 2016"], 1065.0700000000002)
        self.assertEqual(response.data[1]["year - 2015"], 983.03)

    def test_Retrieve_Drug_Reviews_for_a_given_Drug(self):
        response = self.client.post("/sales_and_reviews/Retrieve_Drug_Reviews_for_a_given_Drug/",
                                    {"year": "2016",
                                    "drug": "Melatonin"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 103)
