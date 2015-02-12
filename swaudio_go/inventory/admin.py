from django.contrib import admin
from inventory.models import *

admin.site.register(Item)
admin.site.register(System)
admin.site.register(Locker)

# Register your models here.
