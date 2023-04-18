from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Rooms


# Create your views here.

@login_required(login_url='signup')
def rooms(requests):
    rooms = Rooms.objects.all()
    return render(requests, 'room/rooms.html', {'rooms': rooms})
