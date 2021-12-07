from django.urls import path
from .views import AvailableHotelView

urlpatterns = [
    path('units/', AvailableHotelView.as_view(), name="available_units"),
]
