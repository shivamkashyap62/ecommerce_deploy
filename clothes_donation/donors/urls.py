from django.urls import path
from .views import *

urlpatterns = [
    path("", donation_list, name="donation_list"),
    path("add/", add_donation, name="add_donation"),

    path("<int:donation_id>/requests/", donation_requests, name="donation_requests"),
    path("request/<int:request_id>/<str:status>/", update_request_status, name="update_request_status"),
]