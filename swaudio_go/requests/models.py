from django.db import models
from inventory.models import *
from django.contrib.auth.models import User
import md5

class Reservation(models.Model):
    assigned_system         = models.ForeignKey(System, null=True)
    additional_equipment    = models.ManyToManyField(Item, null=True)
    reservation_name        = models.CharField(max_length=500)
    swatmail                = models.EmailField()
    class_year              = models.IntegerField()
    best_contact_method     = models.CharField(max_length=100)
    other_contact_method    = models.CharField(max_length=500, null=True, blank=True)
    pickup_date             = models.DateField()
    dropoff_date            = models.DateField()
    request_submitted       = models.DateTimeField(editable=False)
    group                   = models.CharField(max_length=500, null=True, blank=True)
    approver                = models.ForeignKey(User, null=True)

    def confirmation_code(self):
        return(md5.md5(str(self.request_submitted)).hexdigest()[3:10].upper())

    def __unicode__(self):
        return "{} {}".format(self.reservation_name, str(self.request_submitted))

class ServiceBlock(models.Model):
    system      = models.ForeignKey(System)
    placed_by   = models.ForeignKey(User)
    reason      = models.TextField()

# Create your models here.
