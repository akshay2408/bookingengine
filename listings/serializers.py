from rest_framework import serializers
from .models import BookingInfo


class ValidateHotelSerializer(serializers.Serializer):
    DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')
    max_price = serializers.IntegerField(required=True)
    check_in = serializers.DateTimeField(input_formats=DATE_INPUT_FORMATS, required=True)
    check_out = serializers.DateTimeField(input_formats=DATE_INPUT_FORMATS, required=True)


class AvailableHotelSerializer(serializers.ModelSerializer):
    listing_type = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()


    class Meta:
        model = BookingInfo
        fields = ["listing_type", "title", "country", "city", "price"]

    def get_listing_type(self, data):
        return data.listing.listing_type if data.listing else None

    def get_title(self, data):
        return data.listing.title if data.listing else None

    def get_country(self, data):
        return data.listing.country if data.listing else None

    def get_city(self, data):
        return data.listing.city if data.listing else None

    def get_price(self, data):
        return data.price
