from email import message
from django.shortcuts import render ,redirect

from django.template import loader
from django.contrib.auth.models import User, auth
from django.contrib import messages

   
from .models import *
'''from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

'''

#===================== Display home page ================================

def index(request):
    return render(request , 'index.html')
#===================================== FORGET PASSWORD ====================

#===================== Catogerizing the Problem statements ===============================
def maintainancedashboard(request):
    ComplaintObj = Complaints.objects.filter(department="maintanence department")
    data = {
        'databasekey' : ComplaintObj
    }
    return render(request , 'Dashbord.html' , data)

def itdashboard(request):
    ComplaintObj = Complaints.objects.filter(department="it infra")
    data = {
        'databasekey' : ComplaintObj
    }
    return render(request , 'Dashbord.html' , data)

def electricdashboard(request):
    ComplaintObj = Complaints.objects.filter(department="electrical department")
    data = {
        'databasekey' : ComplaintObj
    }
    return render(request , 'Dashbord.html' , data)

def messdashboard(request):
    ComplaintObj = Complaints.objects.filter(department="mess coordinator")
    data = {
        'databasekey' : ComplaintObj
    }
    return render(request , 'Dashbord.html' , data)



def addcomplaint(request):
    if request.method == 'POST':
        id_number = request.POST.get('id_number')
        Name = request.POST.get('name')
        Class = request.POST.get('class')
        complaint_txt = request.POST.get('complaint_txt')
        department = request.POST.get('department')
        videoproof=request.FILES.get('videoproof')
        imageproof = request.FILES.get('imageproof')
        complaint  = Complaints(id_number=id_number, Name=Name, complaint_txt=complaint_txt , department=department , videoproof=videoproof , imageproof=imageproof , Class=Class)
        complaint.save()
        return redirect('addcomplaint')

    return render(request, 'Complaint_reg.html')
#========================== Login view ======================================

def login(request):

    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      loginsuccess = auth.authenticate(username=username, password=password)
      if loginsuccess is not None:
        auth.login(request ,loginsuccess)
        if username == 'WATER@WATERADMIN':
            return redirect('maintainancedashboard')
        elif username == 'ITINFRA@ITINFRA':
            return redirect('itdashboard')
        elif username == 'ELECTRICAL@ELECTRICAL':
            return redirect('electricdashboard')
        elif username == 'MESS@MESS':
            return redirect('messdashboard')
        else:
            return redirect('addcomplaint')
      else:
        messages.success(request, ('invalid credentials problem in login'))
        return redirect('login')
        
            
    else:
        return render(request,'index.html' )

def logout(request):
    auth.logout(request)
    return redirect('login')

def showstatus(request):
    if request.user.is_authenticated:
        user=request.user.first_name
        ComplaintObj = Complaints.objects.filter(id_number=user)
        data = {
            'databasekey' : ComplaintObj
        }
        return render(request,'showstatus.html', data )
    else:
        return render(request ,'index.html')
def status(request):
    if request.user.is_authenticated:
        user=request.user.first_name
        ComplaintObj = Complaints.objects.filter(id_number=user).order_by('-date').first()
        data = {
            'databasekey' : ComplaintObj
        }
        return render(request,'status.html', data )
    else:
        return render(request ,'index.html')

def seen(request,pk):
    val = True
    checked = Complaints.objects.get(id=pk)
    checked.seen = True
    checked.save()
    username = request.user.username
    if username == 'WATER@WATERADMIN':
            return redirect('maintainancedashboard')
    elif username == 'ITINFRA@ITINFRA':
        return redirect('itdashboard')
    elif username == 'ELECTRICAL@ELECTRICAL':
        return redirect('electricdashboard')
    elif username == 'MESS@MESS':
        return redirect('messdashboard')
    else:
        return redirect('login')
    
def Deletecomp(request,pk):
    if request.user.is_authenticated:
        solved = Complaints.objects.get(id=pk)
        coppy = Solveddatabase(id_number = solved.id_number , complaint_txt = solved.complaint_txt  , Name = solved.Name , imageproof = solved.imageproof , videoproof = solved.videoproof , Class = solved.Class , date =solved.date , department = solved.department)
        coppy.save()
        ComplaintObj = Complaints.objects.filter(id =pk).delete()
        username = request.user.username
        if username == 'WATER@WATERADMIN':
            return redirect('maintainancedashboard')
        elif username == 'ITINFRA@ITINFRA':
            return redirect('itdashboard')
        elif username == 'ELECTRICAL@ELECTRICAL':
            return redirect('electricdashboard')
        elif username == 'MESS@MESS':
            return redirect('messdashboard')
        else:
            return redirect("addcomplaint")
        
#=============================AUTO REGISTRATION ===================================

def Autoreg(request):
    if request.method =='POST':
        first_name1 = request.POST['first_name'].split("$")
        last_name1 = request.POST['last_name'].split("$")
        email1 = request.POST['email'].split("$")
        username1 = request.POST['username'].split("$")
        password11 = request.POST['password11'].split("$")
        for i in range(len(first_name1)-1):

            first_name = first_name1[i]
            last_name =  last_name1[i]
            email =     email1[i]
            username   = username1[i]
            password1 =password11[i]

            user = User.objects.create_user(email=email , password = password1,username = username ,first_name = first_name ,last_name =last_name)
            user.save()

        return render(request , 'autoreg.html')
    else:
        return render(request , 'autoreg.html')

#========================= Contact us ======================================
        
def Contactus(request):
    return render(request , 'contact.html')
#===================== Display performance ===============================

def Displayperfomance(request):
    electric = len(Complaints.objects.filter(department = "electrical department"))
    maintain = len(Complaints.objects.filter(department="maintanence department"))
    itinfra = len(Complaints.objects.filter(department="it infra"))
    mess = len(Complaints.objects.filter(department="mess coordinator"))
    data = {

        'electric': electric,
        'maintain': maintain,
        'itinfra' : itinfra,
        'mess' : mess
        }
    print(electric)
    return render(request , 'perfomance.html' ,data)







