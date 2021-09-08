from django.shortcuts import render
from .models import JohnGartsu
# Create your views here.
def homepage(request):
    home = JohnGartsu.objects
    return render(request, 'johngartsu/home.html', {'johngartsu': home})
