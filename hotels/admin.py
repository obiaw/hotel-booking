from django.conf import settings
from django.contrib import admin
from .models import Hotel, Rooms
# Register your models here.




# fields = (('hotel_name', 'user'), 'room_type','price','number_available','hotel')

class RoomsAdmin(admin.ModelAdmin):
	def queryset(self, request):
		# qs = super(RoomsAdmin, self).queryset(Hotel.objects.filter(owner_id=request.user))
		# qs = super(RoomsAdmin,self).queryset(Rooms.objects.filter(hotel__owner=request.user))
		qs.hotel.queryset = Hotel.objects.filter(hotel__owner=request.user)
		qs.rooms.queryset = Rooms.objects.filter(hotel__owner=request.user)
		return qs
	def render_change_form(self, request, context, *args, **kwargs):
		 context['adminform'].form.fields['hotel'].queryset = Hotel.objects.filter(owner_id=request.user)
		 return super(RoomsAdmin, self).render_change_form(request, context, *args, **kwargs)
	list_display =('room_type','price','number_available','hotel')

class HotelAdmin(admin.ModelAdmin):

	def queryset(self, request):
		qs.hotel.queryset = Hotel.objects.filter(hotel__owner=request.user)
		qs.rooms.queryset = Rooms.objects.filter(hotel__owner=request.user)
		return qs
		return qs
	list_display = ('name', 'owner')





admin.site.register(Hotel,HotelAdmin)
admin.site.register(Rooms,RoomsAdmin)
admin.site.site_header = "HotelGuide Admin Panel"
admin.site.site_title = "HotelGuide Admin Portal"
admin.site.index_title = "Welcome to HotelGuide Web Portal"
