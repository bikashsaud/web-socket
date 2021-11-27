from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')



def room(request, room_name):
    return render(request, 'chat/room.html', {
    'room_name': room_name
    })


# def room2(request, room_name2):
    # return render(request, 'chat/room.html', {'room_name': room_name2})