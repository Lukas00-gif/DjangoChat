from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from . models import Room

#o decorator de login, paara ve se o usuario esta logado(autenticado)
@login_required
def rooms(request):
    #pega todos as salas que estao listadas
    rooms = Room.objects.all()

    #e retorna para a sala em si
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)

    return render(request, 'room/room.html', {'room': room})

