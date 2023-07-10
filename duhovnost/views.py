from django.shortcuts import render
from .models import Stihovi

# Create your views here.
def home(request):

    queryset = Stihovi.objects.all().order_by('-datum')

    context = {
        'stihovi': queryset
    }
    return render(request, 'home.html', context)

