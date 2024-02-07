from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from employeelogin.models import Employee


# Create your views here.
def dashboard_view(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "dashboard.html")
