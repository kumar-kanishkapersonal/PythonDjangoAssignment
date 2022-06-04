from rest_framework import serializers
from SalesAndReviews.models import PharmaSales
from SalesAndReviews.models import DrugReview


class PharmaSalesSerializer(serializers.ModelSerializer):
    class Meta:
        managed = False
        model = PharmaSales
        fields = '__all__'


class DrugReviewSerializer(serializers.ModelSerializer):
    class Meta:
        managed = False
        model = DrugReview
        fields = '__all__'
