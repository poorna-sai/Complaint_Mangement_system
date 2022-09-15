from email import message
from django.shortcuts import render ,redirect

from django.template import loader
from django.contrib.auth.models import User, auth
from django.contrib import messages
   
from .models import *
'''from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
#read Database
@api_view(['GET'])
def GetComplaint(request):
    Complaintsobj = Complaints.objects.all()
    serializer=ComplaintsSerializer(Complaintsobj,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def PostComplaint(request):
    Complaintsobj = Complaints.objects.all()
    serializer=ComplaintsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

                #### UPDATE######

@api_view(['POST'])
def UpdateComplaint(request ,id):
    Complaintsobj = Complaints.objects.get(id=id)
    serializer=ComplaintsSerializer(instance=Complaintsobj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
    ########DELETE$$#######

@api_view(['DELETE'])
def DeleteComplaint(request ,id):
    Complaintsobj = Complaints.objects.get(id=id)
    Complaintsobj.delete()
    return Response("Succesfully deleted")
    '''

def index(request):
    return render(request , 'index.html')
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
    ComplaintObj = Complaints.objects.filter(id =pk).delete()
        
    return redirect("login")
