from django.shortcuts import render

from .models import Nft
# Create your views here.

def index(request):
    context = { 'nft_list' : Nft.objects.all()}
    return render(request, 'index.html', context)