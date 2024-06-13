from django.shortcuts import render
from .models import ChatgptHelpaivleqa
from .function import *

def index(request):
    return render(request, 'search/index.html')


import csv
from django.shortcuts import render
from django.contrib import messages
from .forms import CSVUploadForm

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This is not a CSV file')
                return render(request, 'upload_csv.html', {'form': form})

            # Read the CSV file and save data to the database
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            print(decoded_file)
            add_db(decoded_file)
            searchdb()
            #for row in reader:
                # Assuming CSV columns are: name, age, email
                # MyModel.objects.create(name=row[0], age=row[1], email=row[2])
                
            messages.success(request, 'File uploaded successfully')
            return render(request, 'search/list.html', {'form': form})
            # return render(request, '/')
    else:
        form = CSVUploadForm()
    
    return render(request, 'search/form.html', {'form': form})


# Create your views here.
def list(request):
    QAlist = ChatgptHelpaivleqa.objects.all()
    catlist = ['모집/선발','교육/수강','국민내일배움카드','채용연계','교육생 지원사항','기타']
    
    search_key = request.GET.get("keyword")
    if search_key:
        QAlist = QAlist.filter(qa__icontains=search_key)
    
    cat_key = request.GET.get("catword")
    if cat_key:
        QAlist = QAlist.filter(pclass=cat_key)
        
    return render(request, 'search/list.html', {'QAlist':QAlist, 'q':search_key, 'catlist':catlist, 'cat':cat_key})