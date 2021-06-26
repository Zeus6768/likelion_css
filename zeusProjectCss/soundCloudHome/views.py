from django.shortcuts import render

# Create your views here.
def discover(request):
    return render(request, "discover.html")