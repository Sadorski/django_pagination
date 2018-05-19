from django.shortcuts import render, HttpResponse, redirect
from models import User
  # the index function is called when root is visited
def index(request):
    context = {
        'users': User.objects.all().order_by('last_name')
    }
    return render(request, 'pagination/index.html', context)

def process(request):
    pass