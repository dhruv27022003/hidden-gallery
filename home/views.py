from distutils.command.upload import upload
from importlib.metadata import files
from operator import contains
from django.shortcuts import render, HttpResponse,redirect
from django.template import context
from .models import file_upload
from django.contrib import messages
from django.core.files import File
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import Myfileupload
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
# import reportlab
# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas
# Create your views here.
class Home(TemplateView):
    template_name='aa.html'

# def index(requests):
#    if requests.method =="POST" :


#     # user = authenticate(username= username, password=password)
#     print("pdf received")
#     f = requests.POST.get('filename')
#     # myfile=File()
#     # myfile = ContentFile(pdf)
#     # instance.structural_info.save('structure.pdf', myfile)
#     f.showPage()
#     f.save()
#     return render(requests,'cb.html',)

#    return render(requests, 'ab.html')
def hiden(requests) :
    if requests.method=="POST":
       form= Myfileupload(requests.POST,requests.FILES)

       if form.is_valid():
           name= form.cleaned_data['file_name']
           the_files = form.cleaned_data['files'] 
           file_upload(file_name=name, my_file=the_files).save()
           return redirect("/view")
       
       else :
             return HttpResponse("ERROR")
 
    else :
           context = {
         'form':Myfileupload()
          }
    return render(requests,'ab.html',context)
   
def index(requests) :
    if requests.method=="POST":
       fo= requests.POST.get('username')
       f3=12345678
       f1= int('0' + fo)
       f2=f3-f1
       print( "yoo boy",f2)
       if (f2==0) :
             print( "yoo man",fo)
             return redirect("view")
       else:
            print( "yoo failed",fo)
            return render(requests,'abb.html')
    return render(requests,'abb.html')
 
def inn(requests) :
    return render(requests,'abb.html') 


def show_file (requests):
     all_files= file_upload.objects.all()

     context = {
         'data': all_files
     }

     return render (requests , 'view.html',context)





def create(request):
     if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        lastname =request.POST.get('NUMBER')
        email =request.POST.get('email')
        
      #   print(username,password,)
        user = User.objects.create_user(username=username,email=email,last_name =lastname, password=password)
        user.save()
        messages.success(request,'YOUR ACCOUNT IS CREATED PLEASE LOGIN NOW')
        return render(request,'login.html')

     return render(request,'create.html')
   

def inde(request):
    print(request.user)
    if request.user.is_anonymous:
     return redirect("/login")
    return render(request, 'index.html')
    #  return HttpResponse('<h1>Page not')


def logi(request):
     if request.method == "POST":
          
        username = request.POST.get('username')
        password = request.POST.get('password')

     #    print(usern,passw,123)
        user = authenticate(username= username, password=password)
        if user is not None:
             # A backend authenticated the credentials
             print(password,12344221)
             login(request,user)
             
             return  redirect("/view")
     
        else:
              
              messages.warning(request,'INVALID')
              return render(request, 'login.html')
         # No backend authenticated the credentials

     return render(request, 'login.html')


def logou(request):
    logout(request)
    messages.success(request,'YOU LOGGED OUT SUCCESSFULLY')
    return redirect("/login")