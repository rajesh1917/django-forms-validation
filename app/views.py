from django.shortcuts import render


from app.forms import *
from django.http import HttpResponse

# Create your views here.

def student(request):
    SF=StudentForm()
    d={'SF':SF}
    if request.method=='POST':
        FD=StudentForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))


    return render(request,'student.html',d)






