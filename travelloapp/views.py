from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinations
# Create your views here.

def index(request):
    dest1 = Destinations()
    dest1.place = 'saudi'
    dest1.desc = 'stay here and win a chance to meet messi'
    dest1.price = 122
    dest1.img = 'destination_3.jpg'
    dest1.offer = False
    
    dest2 = Destinations()
    dest2.place = 'arad'
    dest2.desc = 'stay herdase and win a chance to meet messi'
    dest2.price = 1212
    dest2.img = 'destination_5.jpg'
    dest2.offer = True

    dest3 = Destinations()
    dest3.place = 'saudasdasi'
    dest3.desc = 'stay here and widddn a chance to meet messi'
    dest3.price = 2122
    dest3.img = 'destination_6.jpg'
    dest3.offer = False

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests':dests})