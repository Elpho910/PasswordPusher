from django.shortcuts import render
from .models import TempPassword
import random
import string
from datetime import datetime, timedelta

# Create your views here.


def generate_password():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=10))


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        temp_password = generate_password()
        expiry_date = datetime.now() + timedelta(minutes=60)
        TempPassword.objects.create(
            username=username, temp_password=temp_password, expiry_date=expiry_date
        )
        return render(request, "index.html", {"temp_password": temp_password})
    return render(request, "index.html")
