import random
import string
from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from .models import Item

def core_home(request):
    context = {
        'item': Item.objects.all()
    }
    return render(request, 'core/home.html', context)


