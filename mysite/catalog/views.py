from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.utils.decorators import classonlymethod
from django.views import generic
import csv, io
import datetime
from .models import Data, Pig, Pig_history, Data_history
# Create your views here.



def is_valid_queryparam(param):
    return (param != '' and param is not None)

def check_change(object_history_data, column, fields):
    i = 0
    for field in fields:
        if str(getattr(object_history_data, field)) != str(column[i]):
            return True
        i += 1
    return False

def listfilter(request, model, fields):
    global qs
    qs = model.objects.all()
    for field in fields:
        param = request.GET.get(field)
        if is_valid_queryparam(param):
            qs = qs.filter(**{field:param})
        else:
            param_up_down = ['_min', '_max']
            field_up_down = ['__gte', '__lt']
            for i in range(2):
                param_range = str(field) + str(param_up_down[i])
                field_range = str(field) + str(field_up_down[i])
                param = request.GET.get(param_range)
                print('====', field_range, param, param_range, '====')
                if is_valid_queryparam(param):
                    qs = qs.filter(**{field_range:param})
    return qs
    
def foreignfilter(request, foreignkey, foreignkeyfields, qs):
    for foreignkeyfield in foreignkeyfields:
        field = str(foreignkey) + '__' + str(foreignkeyfield)
        param = request.GET.get(foreignkeyfield)
        if is_valid_queryparam(param):
            qs = qs.filter(**{field:param})
        else:
            param_up_down = ['_min', '_max']
            field_up_down = ['__gte', '__lt']
            for i in range(2):
                param_range = str(foreignkeyfield) + str(param_up_down[i])
                field_range = str(field) + str(field_up_down[i])
                param = request.GET.get(param_range)
                if is_valid_queryparam(param):
                    qs = qs.filter(**{field_range:param})
    return qs
    
def upload_csv(request, model, fields, model_history):
    csv_file = request.FILES['files']
    #Check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF_8')
    io_string = io.StringIO(data_set)
    next(io_string)
    #Upload to the database
    for column in csv.reader(io_string, delimiter=',', quotechar='\\'):
        try:
            object_history_data = model.objects.get(**{fields[0]:column[0]})
            object_history = model_history()
            if check_change(object_history_data, column, fields):
                for field in fields:
                    field_history = getattr(object_history_data, field)
                    setattr(object_history, field, field_history)
                setattr(object_history, 'user', request.user)
                object_history.save()
        except:
            pass
        
        defaults = {}
        for i in range(len(column) - 1):
            defaults[fields[i + 1]] = column[i + 1]
        created = model.objects.update_or_create(**{fields[0]:column[0]}, defaults=defaults) 
    io_string.close()
        
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

def PigListView(request):
    model = Pig
    fields = ['pig_id', 'birth', 'gender', 'dad_id', 'mom_id', 'breed']
    model_history = Pig_history
    template = 'pig_list.html'
    if request.method == 'GET':
        qs = listfilter(request,model,fields)
        context = {'list':qs}
        return render(request,template,context)
    elif request.method == 'POST':
        upload_csv(request, model, fields, model_history)
        qs = listfilter(request,model,fields)
        context = {'list':qs}
        return render(request,template,context)

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

def Pig_HistoryDetailView(request, pk):
    pig_id = pk
    pig_history = Pig_history.objects.filter(pig_id=pig_id)
    context = {'pig_history':pig_history}
    return render(request,'pig_history_detail.html',context)
    
def DataListView(request):
    model = Data
    fields = ['data_id', 'pig_id', 'weight', 'length', 'height', 'front_width', 'back_width', 'depth', 
              'chest', 'front_cannon_circumference', 'back_cannon_circumference', 'date']
    model_history = Data_history
    template = 'data_list.html'
    foreignkey = 'pig_id'
    foreignkeyfields = ['pig_id', 'gender', 'breed', 'birth']
    if request.method == 'GET':
        qs = listfilter(request,model,fields)
        qs = foreignfilter(request, foreignkey, foreignkeyfields, qs)
        context = {'list':qs}
        return render(request,template,context)
    elif request.method == 'POST':
        upload_csv(request, model, fields, model_history)
        qs = listfilter(request,model,fields)
        qs = foreignfilter(request, foreignkey, foreignkeyfields, qs)
        context = {'list':qs}
        return render(request,template,context)

def export_datalist(request):
    '''Refer to https://docs.djangoproject.com/en/3.0/howto/outputting-csv/'''
    #Tell browsers it is a csv file
    response = HttpResponse(content_type='text/csv')
    #File's name
    response['Content-Disposition'] = 'attachment; filename = "data_list.csv"'
    
    #Create a csv file
    writer = csv.writer(response)
    writer.writerow(['Data id', 'Pig id', '重量', '體長', '體高', '前寬', '後寬', '體深', '胸深' ,'前管圍', 
                     '後管圍' ,'拍攝日期'])
    for data in qs:
        writer.writerow([data.data_id, data.pig_id, data.weight, data.length, data.height, data.front_width, 
                         data.back_width, data.depth, data.chest, data.front_cannon_circumference,
                         data.back_cannon_circumference, data.date])
    return response

def Data_HistoryDetailView(request, pk):
    data_id = pk
    data_history = Data_history.objects.filter(data_id=data_id)
    context = {'data_history':data_history}
    return render(request,'data_history_detail.html',context)


class DataDetailView(generic.DetailView):
    model = Data

class PigDetailView(generic.DetailView):
    model = Pig

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PigCreate(CreateView):
    model = Pig
    fields = '__all__'

class Update_with_historyView(UpdateView):
    history_model = None
    
    def post(self, request, *args, **kwargs):
        object_history_data = self.get_object()
        object_history = self.history_model()
        for field in self.fields:
            field_history = getattr(object_history_data, field)
            setattr(object_history, field, field_history)
        setattr(object_history, 'user', request.user)
        object_history.save()
        return super().post(request, *args, **kwargs)


class PigUpdate(Update_with_historyView):
    model = Pig
    history_model = Pig_history
    fields = ['pig_id','birth','gender','dad_id', 'mom_id', 'breed']


class PigDelete(DeleteView):
    model = Pig
    success_url = reverse_lazy('pigs')
