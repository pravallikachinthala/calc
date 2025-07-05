from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    result=None
    if request.method == 'POST':
        a = int(request.POST.get('Num1'))
        b = int(request.POST.get('Num2'))
        opera = request.POST.get('Op')
        if opera == 'add':
            result = a + b
        elif opera == 'mul': result = a * b
        elif opera == 'sub': result = a - b
        elif opera == 'div': result = a // b
        else:
            return render(request,'home.html',{"error":'error'})
       # return render(request,'home.html',{'result':result})
        return redirect('hello',result)
    return render(request,'home.html')
def hello(request,result):
    return render(request,'result.html',{'result':result})