from django import forms
import datetime as dt
from dateutil.relativedelta import relativedelta as rd

class ReservationRequest(forms.Form):
    reservation_name = forms.CharField(label='Your Full Name', max_length=100)
    swatmail = forms.EmailField()
    class_year = forms.ChoiceField(
            choices = [(year, year) for year in range(
                (dt.date.today()+rd(months=+5)).year, (dt.date.today()
                    +rd(months=+5)).year+4)],
            # this is a little trick to make sure the class years are handled
            # properly and updated automatically
            )
    best_contact_method = forms.ChoiceField(
            choices = [
                ('swatmail', "Swatmail"),
                ('other_email', "Other Email"),
                ('text', "Text"),
                ('phone', "Phone"),
                ])
    other_contact_method = forms.CharField(required=False)
    pickup_date = forms.DateField()
    dropoff_date = forms.DateField()
    group = forms.CharField(required=False)
    

