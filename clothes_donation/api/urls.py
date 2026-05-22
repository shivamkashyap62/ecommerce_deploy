from django.urls import path
from .views import *

urlpatterns = [
    path("donations/", DonationListCreateAPI.as_view()),
    path("donations/<int:pk>/", DonationDetailAPI.as_view()),
    path("requests/", RequestListCreateAPI.as_view()),
    path("requests/<int:pk>/", RequestDetailAPI.as_view()),
]