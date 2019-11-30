from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.
def index(request):
    return render(request,'vscode/index.html',{'insert_content':'Initial index page'})

def about(request):
    return render(request,'vscode/about.html')

