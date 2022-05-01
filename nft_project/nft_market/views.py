from django.shortcuts import render

from .models import Nft, User
# Create your views here.

def index(request):
    context = { 'nft_list' : Nft.objects.all()}
    return render(request, 'index.html', context)


def register(request):
    return render(request, 'register.html')


def register_nft(request):
    print(request.POST)
    Nft.objects.create(name=request.POST['name'], introduce=request.POST['introduce']
        , owner= }
    return index(request)