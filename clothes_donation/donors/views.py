from django.shortcuts import render, redirect
from .models import Donation
from django.contrib.auth.decorators import login_required
from receivers.models import Request

@login_required
def donation_list(request):

    donations = Donation.objects.filter(donor=request.user)

    return render(request, "donors/donation_list.html", {
        "donations": donations
    })

@login_required
def add_donation(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        location = request.POST["location"]
        image = request.FILES.get("image")

        Donation.objects.create(
            donor=request.user,
            title=title,
            description=description,
            location=location,
            image=image
        )
        return redirect("donation_list")

    return render(request, "donors/donation_form.html")

@login_required
def donation_requests(request, donation_id):
    donation = Donation.objects.get(id=donation_id, donor=request.user)
    requests = donation.requests.all()
    return render(request, "donors/donation_requests.html", {"donation": donation, "requests": requests})


@login_required
def update_request_status(request, request_id, status):
    req = Request.objects.get(id=request_id)

    if request.user.profile.role != "donor":
        return redirect("home")
    if req.donation.donor != request.user:
        return redirect("donation_list")

    req.status = status
    req.save()
    return redirect("donation_list")