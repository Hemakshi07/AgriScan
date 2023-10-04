from django.shortcuts import render
from .models import DashboardItem
# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Django!")


def dashboard(request):
    # items = DashboardItem.objects.all()
    return render(request, 'agriScanApp/dashboard.html')
