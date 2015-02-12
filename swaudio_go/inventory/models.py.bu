from django.db import models

class Item(models.Model):
    description = models.CharField(max_length=50)
    make        = models.CharField(max_length=100)
    model       = models.CharField(max_length=100)
    def __unicode__(self):
        return self.make + " " + self.model

class System(models.Model):
    letter      = models.CharField(max_length=2)
    color       = models.CharField(max_length=30)
    contents    = models.ManyToManyField(Item)
    
    def __unicode__(self):
        return "System {}".format(self.letter)

    def is_available(self, date):
        '''Returns True or False, if a reservation has already been made for 
        the system on the requested date.  Also returns a flag if the system
        has been reserved but not confirmed'''
        pass


class Locker(models.Model):
    number      = models.IntegerField()
    code        = models.CharField(max_length=10)
    system      = models.ForeignKey(System)

    def __unicode__(self):
        return "Locker {}".format(self.number)
