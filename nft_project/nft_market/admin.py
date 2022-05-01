from django.contrib import admin
from .models import Nft, User, Order

# Register your models here.
admin.site.register(Nft)
admin.site.register(User)
admin.site.register(Order)