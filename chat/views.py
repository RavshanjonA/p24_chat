from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from chat.models import Room, Message


class RoomsView(View):
    def get(self, request):
        rooms = Room.objects.all()
        context = {
            "rooms": rooms
        }
        return render(request, "chat/rooms.html", context)


class RoomView(View):
    def get(self, request, slug):
        room = Room.objects.get(slug=slug)
        messages = Message.objects.filter(room=room)
        context = {
            "room": room,
            "messages": messages
        }
        return render(request, "chat/room.html", context)


class HomeView(TemplateView):
    template_name = "home.html"
