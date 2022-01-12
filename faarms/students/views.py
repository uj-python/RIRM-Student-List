from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from .models import Studentsinfo as si 
from .models import StudentAcademics as sa 
from .serializers import StudentsinfoSerializer as sis
from .serializers import StudentAcademicsSerializer as sas

from .forms import student_academics_form,student_info_form
from django.contrib.auth.forms import UserCreationForm as ucf,AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout

from bs4 import BeautifulSoup
import requests
from django.core.paginator import Paginator 


# Create your views here.

def info(request):
    # st_obj=sl.objects.order_by('FirstName')
    print("inside info")
    st_obj=si.objects.all()
    return render(request,'index.html',{'data':st_obj})

    return HttpResponse("this is student list"+st_obj)
@login_required(login_url='')
def academics(request,rollnumber,name):
    print("user is ",request.user)
    # st_obj=sl.objects.order_by('FirstName')
    st_obj=sa.objects.filter(Roll_No=rollnumber)
    return render(request,'student_details.html',{'data':st_obj,'name':name})

    return HttpResponse("this is student list"+st_obj)

@login_required(login_url='')
def CreateStudent(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['Name'])
        c_info_form=student_info_form(request.POST)
        c_academics_form=student_academics_form(request.POST)
        if c_info_form.is_valid() and c_academics_form.is_valid():
            print("both forms are valid")
            info=c_info_form.save()
            c_info_form.save()
            acd=c_academics_form.save(commit=False)
            # print("---------------------------",acd)
            # print("---------------------------",acd.Maths)
            acd.Roll_No=info
            acd.save()
            return redirect('info')
    info_form=student_info_form()
    academics_form=student_academics_form()
    return render(request,'student_creation.html',{'info_form':info_form,'academics_form':academics_form})

@login_required(login_url='')
def UpdateStudent(request,rollnumber):
    si_obj=si.objects.get(Roll_No=rollnumber)
    sa_obj=sa.objects.get(Roll_No=rollnumber)
    if request.method =='POST':
        c_info_form=student_info_form(request.POST,instance=si_obj)
        c_academics_form=student_academics_form(request.POST,instance=sa_obj)
        if c_info_form.is_valid() and c_academics_form.is_valid():
            print("both forms are valid")
            info=c_info_form.save()
            c_info_form.save()
            acd=c_academics_form.save(commit=False)
            # print("---------------------------",acd)
            # print("---------------------------",acd.Maths)
            acd.Roll_No=info
            acd.save()
            return redirect('info')
    info_form=student_info_form(instance=si_obj)
    academics_form=student_academics_form(instance=sa_obj)
    return render(request,'student_creation.html',{'info_form':info_form,'academics_form':academics_form,'info':si_obj,'academics':sa_obj})

@login_required(login_url='')
def DeleteStudent(request,rollnumber):
    st_obj=sa.objects.get(Roll_No=rollnumber)
    st_obj.delete()
    st_acd=si.objects.get(Roll_No=rollnumber)
    st_acd.delete()
    return redirect('info')


def SearchStudent(request):
    nam=request.POST
    print("------",nam)
    nam=nam['name']
    if nam:
        st_obj=si.objects.filter(Name__icontains=nam)
        if st_obj:
            msg="Student Found"
            return render(request,'index.html',{'data':st_obj,'msg':msg})
        else:
            msg="Student not Found"
            return render(request,'index.html',{'data':st_obj,'msg':msg})

    else:
        msg="input the keyword to search"
        return render(request,'index.html',{'msg':msg})
def register(request):
    if request.method=="POST":
        form=ucf(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('info')
    form=ucf()
    return render(request,'register.html',{'form':form})

def login_view(request):
    msg=""
    print("request is recieved")
    if request.method=="POST":
        print("its post method")
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            print("user authentication successful")
            login(request,user)
            return redirect('info')
        else:
            msg="Enter the valid credentials"
    form=AuthenticationForm()
    return render(request,'login.html',{'form':form,'msg':msg})



def logout_view(request):
    if request.user.is_authenticated:
        print("logging out")
        logout(request)
        return redirect('login')
    else:
        return redirect(request.path_info)





def urlextractor(request):
    urls=[] 
    if request.method=="POST":
        r=request.POST
        site=r['site']
        urls=extract(site)
        print(urls)
    return render(request,'extractor.html',{'urls':urls})


def extract(site):
    print("inside extractor",site)
    urls=[]
    r=requests.get(site)
    s=BeautifulSoup(r.text,"html.parser")
    l=s.find_all("a")
    for i in l:
        if i.has_attr('href'):
            href=i.attrs['href']
            if href.startswith('/'):
                href=site+href[1:]
            if (href not in urls) and href!='javascript:void(0);' and href!="#":
                    urls.append(href)
    return urls
