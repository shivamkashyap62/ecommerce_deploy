from rest_framework import generics
from donors.models import Donation
from receivers.models import Request
from donors.serializers import DonationSerializer
from receivers.serializers import RequestSerializer

class DonationListCreateAPI(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class DonationDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class RequestListCreateAPI(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class RequestDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer