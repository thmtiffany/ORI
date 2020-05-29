from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'resources/resources.html', context)
