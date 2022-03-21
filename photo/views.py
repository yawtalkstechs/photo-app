from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProfileForms
from .models import Profile

# Create your views here.
def home(request):

	if request.method == 'POST':
		form = ProfileForms(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return render(request, 'photo_page.html', {'profiles': Profile.objects.all()})
	else:
		form = ProfileForms()
	return render(request, 'home.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')
