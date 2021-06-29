from django.shortcuts import render, redirect
from .models import Rental
# Create your views here.
def main(request):
    return render(request,'main.html')