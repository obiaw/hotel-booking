from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect
from .models import Rooms,Hotel
from django.contrib.auth.decorators import login_required
from .forms import RoomsForm

# Create your views here.

@login_required(login_url="dashboard/login/")
def home(request):
	# users = request.user
	##u = request.user
	hotel = Hotel.objects.all()
	# hotels =Hotel.objects.filter(user=hotel__user_id).values_list('username', 'email')
	# rooms = Rooms.objects.filter(hotel= hotel)
	# rooms= Rooms.objects.get(hotel__user=u, rooms__hotel=hotels, pk=product_pk) 
	rooms =Rooms.objects.filter(hotel__user=request.user) 
	context ={"rooms":rooms}
	return render(request, 'dashboard.html', context)

## adding new rooms per hotel

def new_room(request):
	form = RoomsForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit= false)
		instance.save()
		return HttpResponseRedirect("home")
		