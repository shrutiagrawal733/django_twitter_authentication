from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request, 'login.html')