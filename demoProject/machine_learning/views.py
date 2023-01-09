from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def machine(request):
    return render(request,'machinelearning.html')

def deepmachine(request):
    return HttpResponse(" <h1>2nd test is done! </h1>")