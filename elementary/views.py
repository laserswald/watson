from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import *


def index(request):
    return render(request, 'elementary/index.html')

def check_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass

### Homework
class HomeworkIndex(generic.ListView):
    template_name = 'elementary/homework/index.html'

    def get_queryset(self):
        return Student.objects.all()

### Schedules and todos
class ScheduleIndex(generic.ListView):
    template_name = 'elementary/schedule/index.html'

    def get_queryset(self):
        return Event.objects.all()

### Wishlist
class WishlistIndex(generic.ListView):
    template_name = 'elementary/wishlist/index.html'

    def get_queryset(self):
        return Wish.objects.all()

### Messages
class MessagesIndex(generic.ListView):
    template_name = 'elementary/messages/index.html'

    def get_queryset(self):
        return Message.objects.all()
