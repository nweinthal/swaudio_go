from django.shortcuts import render
from django.http import HttpResponseRedirect
from requests.forms import ReservationRequest
from requests.models import *
from django.core.mail import send_mail

import datetime as dt

def test(request):
    return render(request, 'helloworld.html',{})

def send_confirmation_email(res):
    to_addr = res.swatmail
    if res.best_contact_method == "other_email":
        to_addr = res.other_contact_method
    cc = res.confirmation_code()
    subject = "Swaudio Go Confirmation {}".format(cc)
    message = "This email is confirmation that we have recieved your request for a Swaudio Go system.  We are processing your request and you will be automatically notified of your assigned system and locker combination within 24 hours of your pickup date.  If for some reason we will be unable to accommodate your request, we will notify you as soon as possible.  \n \n Please feel free to contact us with any questions, \n The Swaudio Team"
    from_addr = 'swaudio.go@gmail.com'
    send_mail(subject, message, from_addr, [to_addr], fail_silently=False)

def send_assignment_email(res):
    to_addr = "nweinthal@gmail.com"
    subject = "New Swaudio Go Request"
    message = "Hello, world"
    from_addr = 'swaudio.go@gmail.com'
    send_mail(subject, message, from_addr, [to_addr], fail_silently=False)

def res_request(request):
    if request.method == 'POST':
        form = ReservationRequest(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_res = Reservation(**data)
            new_res.request_submitted = dt.datetime.now()
            new_res.save()
            #eventually - check availability before saving
            send_confirmation_email(new_res)
            send_assignment_email(new_res)
            message = "Your form was submitted successfully"
    else:
        form = ReservationRequest()
        message  = "This application is currently in development and may behave unpredictably"
    return render(request, 'request_form.html', {"form": form, 'message':message})

# Create your views here.

