from django.shortcuts import render
from .models import Company

# Create your views here.
def homepage(request):
    companies = Company.objects
    return render(request, 'companies/home.html', {'companies': companies})