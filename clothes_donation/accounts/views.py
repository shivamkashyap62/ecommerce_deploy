from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from donors.models import Donation
from receivers.models import Request
from django.contrib.auth.decorators import login_required

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Profile

def home(request):
    return render(request, "home.html")

def register_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        role = request.POST["role"]
        print(f"[DEBUG] Registration attempt for username: '{username}' with role: '{role}'")

        try:
            validate_password(password)

            user = User.objects.create_user(
                username=username,
                password=password
            )

            user.profile.role = role
            user.profile.save()
            print(f"[DEBUG] Registration SUCCESSFUL for username: '{username}'")

            return redirect("login")

        except ValidationError as e:
            print(f"[DEBUG] Registration FAILED for '{username}' due to validation errors: {e.messages}")
            return render(request, "accounts/register.html", {
                "errors": e.messages
            })

    return render(request, "accounts/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(f"[DEBUG] Attempting login for username: '{username}'")
        
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user:
            print(f"[DEBUG] Authentication successful for: '{username}'")
            login(request, user)
            return redirect("home")
        else:
            user_exists = User.objects.filter(username=username).exists()
            print(f"[DEBUG] Authentication FAILED for: '{username}'. Does user exist in DB? {user_exists}")
            
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    role = request.user.profile.role

    context = {"role": role}

    if role == "donor":
        donations = Donation.objects.filter(donor=request.user)
        requests = Request.objects.filter(donation__donor=request.user)

        context.update({
            "total_donations": donations.count(),
            "total_requests": requests.count(),
            "approved_requests": requests.filter(status="approved").count(),
        })

    if role == "receiver":
        requests = Request.objects.filter(receiver=request.user)

        context.update({
            "total_requests": requests.count(),
            "approved_requests": requests.filter(status="approved").count(),
        })

    return render(request, "accounts/dashboard.html", context)