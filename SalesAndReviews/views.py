import csv
import coreapi, coreschema
from rest_framework.schemas import AutoSchema
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from SalesAndReviews.models import PharmaSales
from SalesAndReviews.models import DrugReview
from SalesAndReviews.serializers import PharmaSalesSerializer
from SalesAndReviews.serializers import DrugReviewSerializer

ATC_codes_and_description = {
    "M01AB": "Acetic acid derivatives and related substances",
    "M01AE": "Propionic acid derivatives, antiinflammatory and antirheumatic products",
    "N02BA": "Salicylic acid and derivatives, analgesics and antipyretics",
    "N02BE": "Anilide analgesics and antipyretics",
    "N05B": "ANXIOLYTICS",
    "N05C": "HYPNOTICS AND SEDATIVES",
    "R03": "DRUGS FOR OBSTRUCTIVE AIRWAY DISEASES",
    "R06": "ANTIHISTAMINES FOR SYSTEMIC USE"
}

Drug_Classifiction = {
    "M": "Musculo-Skeletal System Drugs",
    "N": "Nervous System Drugs",
    "R": "Respiratory System Drugs"
}

sales_schema = AutoSchema(
    manual_fields=[coreapi.Field("year", required=True, location="form", schema=coreschema.String()),
                   coreapi.Field("drug_classification", required=True, location="form", schema=coreschema.String())])

review_schema = AutoSchema(
    manual_fields=[coreapi.Field("year", required=True, location="form", schema=coreschema.String()),
                   coreapi.Field("drug", required=True, location="form", schema=coreschema.String())])


class SalesAndReviewsViewSet(viewsets.ViewSet):
    """
    API class
    """
    queryset = PharmaSales.objects.all()

    @action(detail=False, methods=['POST'], schema=sales_schema)
    def Retrieve_Sales_by_Drug_Classification(self, request):
        try:
            year = int(request.data["year"])
            req_drug_classification = request.data["drug_classification"].upper()
            if year not in range(2014, 2020):
                return Response("Year out of range", status=status.HTTP_400_BAD_REQUEST)
            if req_drug_classification not in ["M", "N", "R"]:
                return Response("drug_classification not valid", status=status.HTTP_400_BAD_REQUEST)
            serializer = PharmaSalesSerializer(self.queryset, many=True)
            res = []
            for key in ATC_codes_and_description.keys():
                if key.startswith(req_drug_classification):
                    result = {"drug_classification": Drug_Classifiction[req_drug_classification],
                              "atc_description": f"{ATC_codes_and_description[key]} ({key})"}
                    sales_this_year = 0
                    sales_prev_year = 0
                    this_year = f"year - {year}"
                    prev_year = f"year - {year - 1}"
                    for line in serializer.data:
                        if line.get("year") == year:
                            sales_this_year += line.get(key.lower())
                            result[this_year] = sales_this_year
                        if year - 1 in range(2014, 2020):
                            if line.get("year") == year - 1:
                                sales_prev_year += line.get(key.lower())
                            result[prev_year] = sales_prev_year
                        else:
                            result[prev_year] = "NA"
                    res.append(result)
            return Response(res, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response("Internal Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['POST'], schema=review_schema)
    def Retrieve_Drug_Reviews_for_a_given_Drug(self, request):
            try:
                year = int(request.data["year"])
                drug = request.data["drug"]
                if year not in range(2014, 2020):
                    return Response("Year out of range", status=status.HTTP_400_BAD_REQUEST)
                reviews = DrugReview.objects.filter(drugName=drug).order_by("date")
                if reviews.exists():
                    serializer = DrugReviewSerializer(reviews, many=True)
                    res = []
                    for line in serializer.data:
                        result = {
                            "drug_name": line.get("drugName"),
                            "condition": line.get("condition"),
                            "date": line.get("date"),
                            "review": line.get("review").strip('"\\"'),
                        }
                        res.append(result)
                    return Response(res, status=status.HTTP_200_OK)
                else:
                    return Response("No Reviews Found", status=status.HTTP_404_NOT_FOUND)
            except Exception as exc:
                return Response("Internal Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# # to upload data from csv to db.
# # def uploadPharmaSales(filename):
# #     with open(filename, errors="ignore") as csv_file:
# #         reader = csv.reader(csv_file)
# #         next(reader)
# #         sales_list = []
# #         for row in enumerate(reader):
# #             print(len(row))
# #             (
# #                 _id,
# #                 condition,
# #                 date,
# #                 drugName,
# #                 rating,
# #                 review,
# #                 uniqueId,
# #                 usefulCount,
# #             ) = row[1]
# #             sales_list.append(
# #                 DrugReview(
# #                     _id,
# #                     condition,
# #                     date,
# #                     drugName,
# #                     rating,
# #                     review,
# #                     uniqueId,
# #                     usefulCount,
# #                 )
# #             )
# #     DrugReview.objects.bulk_create(sales_list)
