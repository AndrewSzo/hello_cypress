from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from app.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'dashboard/index.html')


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return render(request, 'dashboard/login.html')


def register(request):
    return render(request, 'registration/signup.html')


def dashboard(request):
    return render(request, 'dashboard/index.html')

# FORMS


def form_layout(request):
    return render(request, 'dashboard/pages/page-form-layout.html')


def form_wizard(request):
    return render(request, 'dashboard/pages/page-form-wizard.html')


# TABLES
def table_basic(request):
    return render(request, 'dashboard/pages/page-table-basic.html')


def table_advance(request):
    return render(request, 'dashboard/pages/page-table-advance.html')

# @login_required(login_url='/accounts/login/')
