from django.shortcuts import render
from .models import ChatgptHelpaivleqa

def index(request):
    return render(request, 'search/index.html')

# Create your views here.

def list(request):
    QAlist = ChatgptHelpaivleqa.objects.all() 
    search_key = request.GET.get("keyword")
    if search_key:
        QAlist = ChatgptHelpaivleqa.objects.filter(qa__icontains=search_key)
    catlist = {qas.pclass for qas in QAlist}
    
    return render(request, 'search/list.html', {'QAlist':QAlist, 'q':search_key, 'catlist':catlist})