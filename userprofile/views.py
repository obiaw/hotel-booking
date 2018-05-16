from django.shortcuts import render ,HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
     user = User.objects.get(username=request.user)
     return render(request,'profile.html',{'user' : user })
    #  return HttpResponse(user.username)

