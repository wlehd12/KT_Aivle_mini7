from django.shortcuts import render
from .models import ChatgptHelpaivleqa

def index(request):
    return render(request, 'search/index.html')

# Create your views here.
def list(request):
    QAlist = ChatgptHelpaivleqa.objects.all()
    catlist = {qas.pclass for qas in QAlist}
    
    search_key = request.GET.get("keyword")
    if search_key:
        QAlist = QAlist.filter(qa__icontains=search_key)
    
    type_query = request.GET.get("type")
    if type_query:
        QAlist = QAlist.filter(pclass=type_query)
        
    return render(request, 'search/list.html', {'QAlist':QAlist, 'q':search_key, 'catlist':catlist})
