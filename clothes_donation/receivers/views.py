from django.shortcuts import render, redirect, get_object_or_404
from .models import Request
from donors.models import Donation
from django.contrib.auth.decorators import login_required

@login_required
def request_list(request):
    requests = Request.objects.filter(receiver=request.user)
    return render(request, "receivers/request_list.html", {"requests": requests})

@login_required
def create_request(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)
    if request.user.profile.role != "receiver":
        return redirect("home")
    if request.method == "POST":
        message = request.POST["message"]
        

        Request.objects.create(
            receiver=request.user,
            donation=donation,
            message=message,
          
        )
        return redirect("request_list")

    return render(request, "receivers/request_form.html", {"donation": donation})

@login_required
def browse_donations(request):

    if request.user.profile.role != "receiver":
        return redirect("home")

    donations = Donation.objects.all()

    return render(request, "receivers/browse_donations.html", {
        "donations": donations
    })