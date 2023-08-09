from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    return render(request, 'hello.html')

# Create your views here.
