from django.shortcuts import render
from .models import ChatgptHelpaivleqa

def index(request):
    return render(request, 'search/index.html')

# Create your views here.
def searchDB(request):
    return request

def list(request):
    QAlist = ChatgptHelpaivleqa.objects.all() 
    search_key = request.GET.get("keyword")
    if search_key:
        QAlist = ChatgptHelpaivleqa.objects.filter(title__icontains=search_key)
    return render(request, 'blog/list.html', {'post_all':QAlist, 'q':search_key})
