from django.shortcuts import render
from ionny.models import *


# Create your views here.


def homepage(request):
    carousel_promoted = Produse.objects.filter(promoted=True)
    context = {
        'carousel_promoted': carousel_promoted
    }
    return render(request, 'home.html', context)


def gallery(request):
    all_pics = Produse.objects.all().order_by('-id')
    context = {
        'all_pics': all_pics,
    }
    return render(request, 'gallery.html', context)


def contact(request):
    contact2 = Contact.objects.all()
    context = {
        'contact2': contact2,
    }

    return render(request, 'contact.html', context)
