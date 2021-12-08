import datetime
from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import ReservedInfo, BookingInfo
from .serializers import AvailableHotelSerializer, ValidateHotelSerializer


class AvailableHotelView(ListAPIView):
    serializer_class = AvailableHotelSerializer

    def get_queryset(self, *args, **kwargs):
        data = self.request.GET
        max_price = data.get('max_price')
        check_in = data.get('check_in')
        check_out = data.get('check_out')

        check_in_date = datetime.datetime.strptime(check_in, "%Y-%m-%d").date()
        check_out_date = datetime.datetime.strptime(check_out, "%Y-%m-%d").date()
        booked_id = ReservedInfo.objects.filter(check_in__date__lte=check_out_date).filter(
            check_out__date__gte=check_in_date).values_list('booking_info_id', flat=True)
        qs = BookingInfo.objects.filter(price__lte=max_price).filter(Q(hotel_room_type__isnull=False)
                                                                    |Q(listing__isnull=False)).exclude(id__in=booked_id).order_by("price")
        return qs

    def list(self, request, *args, **kwargs):
        hotel_serializer = ValidateHotelSerializer(data=self.request.GET)
        hotel_serializer.is_valid(raise_exception=True)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
