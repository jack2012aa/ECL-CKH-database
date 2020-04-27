from django.shortcuts import render
from django.contrib import messages

from django.http import HttpResponse
import csv, io
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
    
def PigListView(request):
    context = {
        'pig_list': Pig.objects.all(),
        }
    #GET request
    if request.method == 'GET':
        return render(request, 'pig_list.html', context=context)
    
    #POST request
    ''''Refer to https://medium.com/@simathapa111/how-to-upload-a-csv-file-in-django-3a0d6295f624'''
    #Get uploaded file
    csv_file = request.FILES['files']
    #Check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF_8')
    io_string = io.StringIO(data_set)
    next(io_string)
    #Upload to the database
    for column in csv.reader(io_string, delimiter=',', quotechar='\\'):
        created = Pig.objects.update_or_create(
            pig_id=column[0],
            birth=column[1],
            gender=column[2],
            dad_id=column[3],
            mom_id=column[4],
            breed=column[5],
            )
    io_string.close()
    return render(request, 'pig_list.html', context=context)

def export_piglist(request):
    '''Refer to https://docs.djangoproject.com/en/3.0/howto/outputting-csv/'''
    #Tell browsers it is a csv file
    response = HttpResponse(content_type='text/csv')
    #File's name
    response['Content-Disposition'] = 'attachment; filename = "pig_list.csv"'
    
    #Create a csv file
    writer = csv.writer(response)
    writer.writerow(['Pig id', 'Birthday', 'Gender', 'Dad id', 'Mom id', 'Breed'])
    for pig in Pig.objects.all():
        writer.writerow([pig.pig_id, pig.birth, pig.gender, pig.dad_id, pig.mom_id, pig.breed])
    return response

class DataDetailView(generic.DetailView):
    model = Data
    ''' if writen in function view
    def book_detail_view(request, primary_key):
        try:
            data = Data.objects.get(pk=primary_key)
        except Data.DoesNotExist:
            raise Http404('Book does not exist')

        from django.shortcuts import get_object_or_404
        data = get_object_or_404(Data, pk=primary_key)
        
        return render(request, 'catalog/data_detail.html', context={'data': data})
    '''

class PigDetailView(generic.DetailView):
    model = Pig
    ''' if writen in function view
    def pig_detail_view(request, primary_key):
        try:
            pig = pig.objects.get(pk=primary_key)
        except Pig.DoesNotExist:
            raise Http404('Pig does not exist')

        from django.shortcuts import get_object_or_404
        pig = get_object_or_404(Pig, pk=primary_key)
        
        return render(request, 'catalog/pig_detail.html', context={'pig': pig})
        '''
