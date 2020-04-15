from django.shortcuts import render

# from django.http import HttpResponse
from datetime import datetime
# Create your views here.

from .models import Data, Pig

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_datas = Data.objects.all().count()
    
    # The 'all()' is implied by default.    
    num_pigs = Pig.objects.count()
    num_datas = Data.objects.count()
    
    context = {
        'num_datas': num_datas,
        'num_pigs': num_pigs,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic
class DataListView(generic.ListView):
    model = Data
    
class PigListView(generic.ListView):
    model = Pig

class DataDetailView(generic.DetailView):
    model = Data
    def book_detail_view(request, primary_key):
        try:
            data = Data.objects.get(pk=primary_key)
        except Data.DoesNotExist:
            raise Http404('Book does not exist')

        from django.shortcuts import get_object_or_404
        data = get_object_or_404(Data, pk=primary_key)
        
        return render(request, 'catalog/data_detail.html', context={'data': data})

class PigDetailView(generic.DetailView):
    model = Pig
    def pig_detail_view(request, primary_key):
        try:
            pig = pig.objects.get(pk=primary_key)
        except Pig.DoesNotExist:
            raise Http404('Pig does not exist')

        from django.shortcuts import get_object_or_404
        pig = get_object_or_404(Pig, pk=primary_key)
        
        return render(request, 'catalog/pig_detail.html', context={'pig': pig})
