from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class UserProfileSignalTest(TestCase):
    def test_user_creation_creates_profile(self):
        user = User.objects.create_user(username="testuser", password="testpassword123")
        self.assertTrue(Profile.objects.filter(user=user).exists())
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.user.username, "testuser")
        
    def test_profile_str_representation(self):
        user = User.objects.create_user(username="testuser_str", password="testpassword123")
        profile = Profile.objects.get(user=user)
        self.assertEqual(str(profile), "testuser_str")
