from django.shortcuts import redirect, render
from prep.forms import UserRegisterFor
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserRegisterFor(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return render (request,'login.html',{'success':"no errrorrrrrrrrrr"})
        else:
            error_message=form.errors.as_text()
            return render(request,'register.html',{'error':"here is a error"})
        
    return render(request,'register.html')

def login_up(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            return render(request,'home.html')
        else:
            return render(request,'login.html',{'error':"not verified occured"})    
    
    return render(request,'login.html')

@login_required
def home(request):
    return render(request,"home.html")
@login_required
def logout(request):
    logout(request)
    return render(request,'login')