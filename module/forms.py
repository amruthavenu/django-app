from django import forms
from .models import Table, Hotel

class Tableform(forms.ModelForm):
    class Meta:
        model= Table
        fields = '__all__'


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']
