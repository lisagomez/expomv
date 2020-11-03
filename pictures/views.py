from django.shortcuts import render
from .models import Picture

def index(request):
    pictures= Picture.objects.all()
    context= {'pictures':pictures}
    return render(request, 'pictures/index.html', context)