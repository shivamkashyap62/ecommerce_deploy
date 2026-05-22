from django.db import models
from django.contrib.auth.models import User
from donors.models import Donation


STATUS_CHOICES = [
    ("pending", "Pending"),
    ("approved", "Approved"),
    ("rejected", "Rejected"),
]

class Request(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, related_name="requests")
    message = models.TextField()
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.receiver.username} → {self.donation.title}"