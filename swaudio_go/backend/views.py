from django.shortcuts import render
from django.contrib.auth import *
from requests.forms import ReservationRequest

def logout_view(request):
    logout(request)
    return render(request, 'request_form.html', {'form': ReservationRequest(), 
        'message': "You have successfully logged out"})

def login_view(request):
    #TODO get the login system working 
    pass
# Create your views here.
