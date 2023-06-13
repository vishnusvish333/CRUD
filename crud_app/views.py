from django.shortcuts import get_object_or_404, redirect, render
from .models import crud
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')
            
        user= User.objects.create_user(username=username,email=email,password=password1)
        user.save();
        print("user created")
        return redirect('login')

   
    return render(request,'signup.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        user= auth.authenticate(username=username,password=password1)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('add')
        else:
            return render(request,'login.html')
    return render(request,'login.html')


def add(request):
    task1 = crud.objects.all()
    if request.method=='POST':
        slno=request.POST.get('slno','')
        itemname=request.POST.get('itemname','')
        desc=request.POST.get('desc','')
        task=crud(sl_no=slno,item_name=itemname,description=desc)
        task.save()
        messages.success(request, 'Data added successfully.')
    return render(request,'index.html',{'task':task1})

def delete(request,id):
    task=crud.objects.get(id=id)
    
    task.delete()
    return redirect('/')

def update(request,id):
    task=get_object_or_404(crud,id=id)
    if request.method == 'POST':
        task.sl_no = request.POST.get('slno')
        task.item_name = request.POST.get('itemname')
        task.description = request.POST.get('desc')
        task.save()
        return redirect('/')
    return render(request,'update.html',{'task':task})

    