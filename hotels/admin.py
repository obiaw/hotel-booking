from django.contrib import admin
from .models import Hotel, Rooms
# Register your models here.



# fields = (('hotel_name', 'user'), 'room_type','price','number_available','hotel')

class RoomsAdmin(admin.ModelAdmin):
	list_display =('room_type','price','number_available','hotel')

class HotelAdmin(admin.ModelAdmin):
	list_display = ('name', 'user')

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Rooms,RoomsAdmin)

