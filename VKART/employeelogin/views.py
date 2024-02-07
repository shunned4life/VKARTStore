from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from employeelogin.models import Employee


# Create your views here.
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #TODO check database instead of save
            form.save()

    context = {'form': form}
    return render(request, 'login.html', context)


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your account has been created')

            # return redirect(dashboard)

    context = {'form': form}
    return render(request, 'register.html', context)
