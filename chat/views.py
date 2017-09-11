from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from chat.models import ChatRoom
# Create your views here.



def index(request):
    chat_rooms= ChatRoom.objects.name[:5]
    context = {
        'chat_list' : chat_rooms
    }
    return render(request,'chat/index.html', context)


def chat_room(request,chat_room_id):
    chat = get_object_or_404(ChatRoom, pk =chat_room_id)
    return render(request,'chat/chat_room.html', {'chat':chat})
