from django.shortcuts import render # type: ignore
from .models import Destination
# Create your views here.


def index (request):

    # dest1 = Destination()
    # dest1.name = "Sindhuli"
    # dest1.desc = "The Historic place of Nepal"
    # dest1.img = "destination_1.jpg"
    # dest1.price = 700
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = "Kathmandu"
    # dest2.desc = "The Capital City of Nepal"
    # dest2.img = "destination_2.jpg"
    # dest2.price = 800
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = "Bhaktapur"
    # dest3.desc = "The smallest District of Nepal"
    # dest3.img = "destination_3.jpg"
    # dest3.price = 900
    # dest3.offer = False

    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()

    return render (request, "index.html", {'dests': dests })