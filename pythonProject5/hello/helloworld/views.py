from django.shortcuts import render


# Create your views here.

def index(request):
    name = "india"
    return render(request, 'index.html', {'obj': name})
def add(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    sum=x+y
    return render(request, "result.html", {'sum':sum})
def average(request):
    return render(request, 'average.html')
def ave(request):
    x=int(request.GET['n1'])
    y=int(request.GET['n2'])
    z=int(request.GET['n3'])
    ave = (x+y+z)/3
    return render(request, "avresult.html", {'average': ave})