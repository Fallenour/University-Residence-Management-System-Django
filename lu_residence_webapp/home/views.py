from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def landing(request):
    return render(request, '../../common/templates/home/landing.html')


def news(request):
    return render(request, '../../common/templates/home/news.html')


def housing(request):
    return render(request, '../../common/templates/home/housing.html')


def fees(request):
    return render(request, '../../common/templates/fees/fees.html')


def work_order(request):
    return render(request, '../../common/templates/workorder/workorder.html')


def repair_form(request):
    return render(request, '../../common/templates/workorder/townhouse_repair.html')


def bartley(request):
    return render(request, '../../common/templates/workorder/bartley.html')


def north_res(request):
    return render(request, '../../common/templates/workorder/north_residence.html')


def south_res(request):
    return render(request, '../../common/templates/workorder/south_residence.html')


def faq(request):
    return render(request, '../../common/templates/faq/faq.html')
def apply(request):
    return render(request, '../../common/templates/apply/apply.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:news')
    else:
        form = UserCreationForm()
    return render(request, '../../common/templates/registration/register.html', {'form': form})
