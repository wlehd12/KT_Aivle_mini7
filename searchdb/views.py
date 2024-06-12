from django.shortcuts import render
from .models import ChatgptHelpaivleqa

def index(request):
    return render(request, 'search/index.html')

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