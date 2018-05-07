from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import Rooms, Hotel
from django.contrib.auth.decorators import login_required
from .forms import RoomsForm


# Create your views here.

@login_required(login_url="dashboard/login/")
def home(request):
    if request.user:
        rooms = Rooms.objects.filter(hotel__owner=request.user)
        hotel = Hotel.objects.filter(owner_id=request.user)
    context = {"rooms": rooms, "hotel": hotel}
    return render(request, 'dashboard.html', context)


## adding new rooms per hotel

@login_required(login_url="dashboard/login/")
def new_room(request):
    if request.method == 'POST':
        form = RoomsForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            rooms = Rooms.objects.filter(hotel__owner=request.user)
            for r in rooms:
                instance.hotel_id = r.hotel_id
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/dashboard')
    else:
        form = RoomsForm()
    return render(request, 'newroom_form.html', {"form": form})

