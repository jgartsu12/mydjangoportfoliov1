from django.shortcuts import render, get_object_or_404
from .models import Company


# Create your views here.
def homepage(request):
    companies = Company.objects
    return render(request, 'companies/home.html', {'companies': companies})

def detail(request, company_id):
    company_detail = get_object_or_404(Company, pk=company_id)
    return render(request, 'companies/detail.html', {'company':company_detail})