from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse

def insert_student(request):
    SEFO=StudentForm()
    d={'SEFO':SEFO}

    if request.method=='POST':
        SDFO=StudentForm(request.POST)
        if SDFO.is_valid():
            Sname=SDFO.cleaned_data['Sname']
            Sid=SDFO.cleaned_data['Sid']
            Sage=SDFO.cleaned_data['Sage']
            Semail=SDFO.cleaned_data['Semail']

            SO=Student.objects.get_or_create(Sname=Sname,Sid=Sid,Sage=Sage,Semail=Semail)[0]
            SO.save()

            QSO=Student.objects.all()
            d1={'QSO':QSO}
            return render(request,'display_student.html',d1)
            #return HttpResponse(str(SDFO.cleaned_data))

    return render(request,'insert_student.html',d)

