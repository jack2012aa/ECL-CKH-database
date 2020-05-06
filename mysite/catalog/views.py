from django.shortcuts import render
from django.contrib import messages

from django.http import HttpResponse
import csv, io
# Create your views here.

from .models import Data, Pig

def is_valid_queryparam(param):
    return (param != '' and param is not None)

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

def DataListFilter(request):
    #Generate filter from request
    '''Refer to https://github.com/justdjango/djfilter'''
    #global variable for export
    global qs
    qs = Data.objects.all()
    data_id = request.GET.get('data_id')
    pig_id = request.GET.get('pig_id')
    pig_gender = request.GET.get('pig_gender')
    pig_breed = request.GET.get('pig_breed')
    pig_birth_min = request.GET.get('pig_birth_min')
    pig_birth_max = request.GET.get('pig_birth_max')
    data_weight_min = request.GET.get('data_weight_min')
    data_weight_max = request.GET.get('data_weight_max')
    data_length_min = request.GET.get('data_length_min')
    data_length_max = request.GET.get('data_length_max')
    data_height_min = request.GET.get('data_height_min')
    data_height_max = request.GET.get('data_height_max')
    data_front_width_min = request.GET.get('data_front_width_min')
    data_front_width_max = request.GET.get('data_front_width_max')
    data_back_width_min = request.GET.get('data_back_width_min')
    data_back_width_max = request.GET.get('data_back_width_max')
    data_depth_min = request.GET.get('data_depth_min')
    data_depth_max = request.GET.get('data_depth_max')
    data_chest_min = request.GET.get('data_chest_min')
    data_chest_max = request.GET.get('data_chest_max')
    data_front_cir_min = request.GET.get('data_front_cir_min')
    data_front_cir_max = request.GET.get('data_front_cir_max')
    data_back_cir_min = request.GET.get('data_back_cir_min')
    data_back_cir_max = request.GET.get('data_back_cir_max')
    data_date_min = request.GET.get('data_date_min')
    data_date_max = request.GET.get('data_date_max')
        
    if is_valid_queryparam(data_id):
        qs = qs.filter(data_id=data_id)

    if is_valid_queryparam(pig_id):
        qs = qs.filter(pig_id__pig_id=pig_id) 
            
    if is_valid_queryparam(pig_gender):
        qs = qs.filter(pig_id__gender=pig_gender)
        
    if is_valid_queryparam(pig_breed):
        qs = qs.filter(pig_id__breed=pig_breed)
        
    if is_valid_queryparam(pig_birth_min):
        qs = qs.filter(pig_id__birth__gte=pig_birth_min)

    if is_valid_queryparam(pig_birth_max):
        qs = qs.filter(pig_id__birth__lt=pig_birth_max)
        
    if is_valid_queryparam(data_weight_min):
        qs = qs.filter(weight__gte=data_weight_min)   

    if is_valid_queryparam(data_weight_max):
        qs = qs.filter(weight__lt=data_weight_max)
        
    if is_valid_queryparam(data_length_min):
        qs = qs.filter(length__gte=data_length_min)

    if is_valid_queryparam(data_length_max):
        qs = qs.filter(length__lt=data_length_max)
        
    if is_valid_queryparam(data_height_min):
        qs = qs.filter(height__gte=data_height_min)

    if is_valid_queryparam(data_height_max):
        qs = qs.filter(height__lt=data_height_max)
        
    if is_valid_queryparam(data_front_width_min):
        qs = qs.filter(front_width__gte=data_front_width_min)  

    if is_valid_queryparam(data_front_width_max):
        qs = qs.filter(front_width__lt=data_front_width_max)
        
    if is_valid_queryparam(data_back_width_min):
        qs = qs.filter(back_width__gte=data_back_width_min)

    if is_valid_queryparam(data_back_width_max):
        qs = qs.filter(back_width__lt=data_back_width_max)
        
    if is_valid_queryparam(data_depth_min):
        qs = qs.filter(depth__gte=data_depth_min)

    if is_valid_queryparam(data_depth_max):
        qs = qs.filter(depth_lt=data_depth_max)
        
    if is_valid_queryparam(data_chest_min):
        qs = qs.filter(chest__gte=data_chest_min)  
            
    if is_valid_queryparam(data_chest_max):
        qs = qs.filter(chest__lt=data_chest_max)
        
    if is_valid_queryparam(data_front_cir_min):
        qs = qs.filter(front_cannon_circumference__gte=data_front_cir_min)

    if is_valid_queryparam(data_front_cir_max):
        qs = qs.filter(front_cannon_circumference__lt=data_front_cir_max)
        
    if is_valid_queryparam(data_back_cir_min):
        qs = qs.filter(back_cannon_circumference__gte=data_back_cir_min)

    if is_valid_queryparam(data_back_cir_max):
        qs = qs.filter(data_back_cir_max=data_back_cir_max)
        
    if is_valid_queryparam(data_date_min):
        qs = qs.filter(date__gte=data_date_min)  

    if is_valid_queryparam(data_date_max):
        qs = qs.filter(date__lt=data_date_max)
        
    return qs


def PigListFilter(request):
    #Generate filter from request
    '''Refer to https://github.com/justdjango/djfilter'''
    #global variable for export
    global qs
    qs = Pig.objects.all()
    pig_id = request.GET.get('pig_id')
    pig_gender = request.GET.get('pig_gender')
    pig_breed = request.GET.get('pig_breed')
    pig_dad_id = request.GET.get('pig_dad_id')
    pig_mom_id = request.GET.get('pig_mom_id')
    pig_birth_from = request.GET.get('pig_birth_from')
    pig_birth_to = request.GET.get('pig_birth_to')
    

    if is_valid_queryparam(pig_id):
        qs = qs.filter(pig_id=pig_id) 
            
    if is_valid_queryparam(pig_gender):
        qs = qs.filter(gender=pig_gender)
        
    if is_valid_queryparam(pig_breed):
        qs = qs.filter(breed=pig_breed)

    if is_valid_queryparam(pig_dad_id):
        qs = qs.filter(dad_id=pig_dad_id) 

    if is_valid_queryparam(pig_mom_id):
        qs = qs.filter(mom_id=pig_mom_id)

    if is_valid_queryparam(pig_birth_from):
        qs = qs.filter(birth__gte=pig_birth_from)

    if is_valid_queryparam(pig_birth_to):
        qs = qs.filter(birth__lt=pig_birth_to)
        
    return qs


def DataListView(request):
    if request.method == 'GET':
        context = {'data_list': DataListFilter(request)}
        return render(request, 'data_list.html', context)
    
    if request.method =='POST':
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
                created = Data.objects.update_or_create(
                pig_id=Pig.objects.filter(pig_id=column[0])[0],
                weight=column[1],
                length=column[2],
                height=column[3],
                front_width=column[4],
                back_width=column[5],
                depth=column[6],
                chest=column[7],
                front_cannon_circumference=column[8],
                back_cannon_circumference=column[9],
                date=column[10],
                )
            io_string.close()
        context = {'data_list': DataListFilter(request)}
        return render(request, 'data_list.html', context=context)


def PigListView(request):
    #GET request
    if request.method == 'GET':
        context = {'pig_list': PigListFilter(request)}
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
    context = {'pig_list': PigListFilter(request)}
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
    # for pig in Pig.objects.all():
    for pig in qs:
        writer.writerow([pig.pig_id, pig.birth, pig.gender, pig.dad_id, pig.mom_id, pig.breed])
    return response

def export_datalist(request):
    '''Refer to https://docs.djangoproject.com/en/3.0/howto/outputting-csv/'''
    #Tell browsers it is a csv file
    response = HttpResponse(content_type='text/csv')
    #File's name
    response['Content-Disposition'] = 'attachment; filename = "data_list.csv"'
    
    #Create a csv file
    writer = csv.writer(response)
    writer.writerow(['Pig id', '重量', '體長', '體高', '前寬', '後寬', '體深', '胸深' ,'前管圍', 
                     '後管圍' ,'拍攝日期'])
    for data in qs:
        writer.writerow([data.pig_id, data.weight, data.length, data.height, data.front_width, 
                         data.back_width, data.depth, data.chest, data.front_cannon_circumference,
                         data.back_cannon_circumference, data.date])
    return response

class DataDetailView(generic.DetailView):
    model = Data
    ''' if writen in function view
    def data_detail_view(request, primary_key):
        try:
            data = Data.objects.get(pk=primary_key)
        except Data.DoesNotExist:
            raise Http404('Data does not exist')

        from django.shortcuts import get_object_or_404
        data = get_object_or_404(Data, pk=primary_key)
        
        return render(request, 'catalog/data_detail.html', context={'data': data})
        '''


class PigDetailView(generic.DetailView):
    model = Pig
    
    #  if writen in function view
    def pig_detail_view(request, primary_key):
        try:
            pig = pig.objects.get(pk=primary_key)
        except Pig.DoesNotExist:
            raise Http404('Pig does not exist')

        from django.shortcuts import get_object_or_404
        pig = get_object_or_404(Pig, pk=primary_key)
        
        return render(request, 'catalog/pig_detail.html', context={'pig': pig})
    

def edit_pig(request):
    return render(request, 'edit_pig.html')
