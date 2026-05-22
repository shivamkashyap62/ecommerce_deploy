from django.urls import path
from .views import *

urlpatterns = [
    path("", request_list, name="request_list"),
    path("create/<int:donation_id>/", create_request, name="create_request"),
    path("browse/", browse_donations, name="browse_donations"),
]