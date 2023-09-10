from django.shortcuts import render, get_object_or_404, redirect
from .models import TempPassword
import random
import string
from datetime import datetime, timedelta
import uuid

# Create your views here.


def generate_password():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=10))


def generate_link():
    return uuid.uuid4()


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        temp_password = "InsertPasswordHere"
        expiry_date = datetime.now() + timedelta(minutes=60)
        link = generate_link()
        TempPassword.objects.create(
            username=username,
            temp_password=temp_password,
            expiry_date=expiry_date,
            link=link,
        )

        return render(request, "index.html", {"link": link})
    return render(request, "index.html")


def view_password(request, link):
    temp_pass_obj = get_object_or_404(TempPassword, link=link)
    if (
        temp_pass_obj.view_count >= temp_pass_obj.max_views
        or datetime.now() > temp_pass_obj.expiry_date
    ):
        temp_pass_obj.delete()
        return render(request, "expired.html")

    temp_pass_obj.view_count += 1
    temp_pass_obj.save()

    if temp_pass_obj.view_count >= temp_pass_obj.max_views:
        temp_pass_obj.delete()

    return render(
        request, "view_password.html", {"temp_password": temp_pass_obj.temp_password}
    )
