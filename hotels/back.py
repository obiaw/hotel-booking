from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect
from .models import Rooms,Hotel
from django.contrib.auth.decorators import login_required
from .forms import RoomsForm

# Create your views here.

@login_required(login_url="dashboard/login/")
def home(request):
	# users = request.user
	##u = request.user
	# hotel = Hotel.objects.all()
	# hotels =Hotel.objects.filter(user=hotel__user_id).values_list('username', 'email')
	# rooms = Rooms.objects.filter(hotel= hotel)
	# rooms= Rooms.objects.get(hotel__user=u, rooms__hotel=hotels, pk=product_pk) 
	if request.user:
		rooms =Rooms.objects.filter(hotel__owner=request.user)
		hotel = Hotel.objects.filter(owner_id=request.user) 
	context ={"rooms":rooms,"hotel": hotel}
	return render(request, 'dashboard.html', context)

## adding new rooms per hotel

@login_required(login_url="dashboard/login/")
def new_room(request,pk=None):
	# form = RoomsForm
	# if form.is_valid():
	# 	instance = form.save(commit=False)
	# 	instance.user = request.user
	# 	instance.save()
	# 	return HttpResponseRedirect("home")
	# cont = {"form": form } 
	# f = form(request.POST or None)
	# return render(request,'newroom_form.html', cont)
	# if request.method == 'POST':
		# f = RoomsForm(request.POST or None)
		# if f.is_valid():
			# new_room = f.save(commit=False)
			# new_room.user = request.user
			# new_room.rooms = Rooms.objects.filter(hotel__user=request.user, hotel__id = hotel_id)
			# new_room.hotel = Hotel.objects.filter(user_id=request.user, rooms__hotel =rooms.hotel_id) 
			# new_room.hotel_id = Rooms.objects.filter(rooms__hotel_id =rooms.hotel_id)
			# new_room.hotel = hotel
			# print(new_room.hotel_id)
			# new_room.save()
			# return HttpResponseRedirect("home")
		# else:
			# f = RoomsForm(request.user,request.POST)
	# return render(request,'newroom_form.html', {"form":f})
	# if request.method =='POST':
	# 	# owner=Hotel.objects.get(hotel__owner=request.id)
	# 	# room = get_object_or_404(Rooms,hotel_id=rooms.hotel_id)
	# 	form = RoomsForm(request.POST or None)
	# 	if form.is_valid():
	# 		instance = form.save(commit=False)
	# 		instance.owner = Hotel.objects.filter(hotel__owner = request.owner)
	# 		# instance.rooms = room
	# 		instance.save()
	# 		return HttpResponseRedirect('home')
	# else:
	# 	form = RoomsForm(request.POST or None)
	# return render(request,'newroom_form.html', {"form":form})

	if request.user:
		form=RoomsForm(request.POST or None)
		if form.is_valid():
			# data=form.cleaned_data
			# newbookdate.hotel=Hotel(owner=request.user,hotel=Rooms.objects.get(hotel_id=hotel_id),rooms=data['rooms'])
			# newbookdate.hotel 
			newbookdate = form.save(commit=False)
			newbookdate.owner = request.user
			# h = Hotel.objects.get(pk=id)
			hotel_id = Rooms.objects.get(hotel_id=1)
			# newbookdate.hotel_id =Rooms.objects.get(hotel__hotel__id = hotel__rooms.hotel_id)
			newbookdate.hotel = hotel_id
			# newbookdate = data['rooms']
			newbookdate.save()
			return HttpResponseRedirect('/')
	else:
		form = RoomsForm(request.POST or None)
		# context = {
  #           'form': RoomsForm(hotel_id=hotel_id),
  #           'hotel': Rooms.objects.get(hotel_id=hotel_id)
  #       }
	return render(request,'newroom_form.html', {"form":form})


		