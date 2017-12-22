from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print("It was a POST request")
    return HttpResponse('Hello World!')
