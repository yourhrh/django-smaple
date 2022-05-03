from django.shortcuts import render

from .models import Nft, User
# Create your views here.

def index(request):
    context = { 'nft_list' : nft.objects.all()}
    return render(request, 'index.html', context)


def register(request):
    return render(request, 'register.html')


def register_nft(request):
    print(request.POST)
    first_user = User.objects.get()
    Nft.objects.create(name=request.POST['name'], introduce=request.POST['introduce']
        , owner=first_user, image_url=request.POST['image_url'], min_price=request.POST['min_price'])
    return index(request)