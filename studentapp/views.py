import os
from django.shortcuts import render,redirect
from studentapp.models import studentdetails
# Create your views here.
def addstudent(request):
    return render(request,'add.html')

def addstudentdetails(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        contact=request.POST['contact']
        course=request.POST['course']
        email=request.POST['email']
        address=request.POST['address']
        image=request.FILES.get('file')

        students=studentdetails(firstname=firstname,lastname=lastname,contact=contact,course=course,
                               email=email,address=address,image=image)
        students.save()
        print('hlo')
        return redirect('showstudent')
    
def showstudent(request):
    students=studentdetails.objects.all()
    return render(request,'show.html',{'students':students})



def proflpage(request,pk):
    students=studentdetails.objects.get(id=pk)
    return render(request,'profl.html',{'students':students})

def edit2sdtdetails(request,pk):
    if request.method=='POST':
        students=studentdetails.objects.get(id=pk)
        old=students.image
        new=request.FILES.get('file')
        if old !=None and new==None:
            students.image=old
        else:
            students.image=new
        students.firstname=request.POST.get('firstname')
        students.lastname=request.POST.get('lastname')
        students.contact=request.POST.get('contact')
        students.course=request.POST.get('course')
        students.email=request.POST.get('email')
        students.address=request.POST.get('address')
        students.save()
        return redirect('showstudent')
    return render(request,'profl.html',{'students':students})



def deletepage(request,pk):
    students=studentdetails.objects.get(id=pk)
    return render(request,'delete.html',{'students':students})

def deletestudent(request,pk):
    students=studentdetails.objects.get(id=pk)
    students.delete()
    return redirect('showstudent')
    
def delete(request, pk):
     students=studentdetails.objects.get(id=pk)
     students.image = ""
     students.save()
     return render(request,'profl.html',{'students':students})


        