from django.shortcuts import render
from .forms import PostForm
import sys
from .res.classifier import calculate_flare, testing
data = []
def index(request):
	
	if request.method == "POST":
		print(request.POST['url'])
		data = calculate_flare(request.POST['url'])
		
	return render(request, 'index.html', {'data' : data})

def automated_testing(request):

	if request.method == "POST":
		print(request.POST)
		json = testing(request.POST)
	return render(request, 'testing.html')