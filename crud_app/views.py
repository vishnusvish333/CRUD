from django.shortcuts import get_object_or_404, redirect, render
from .models import crud
from django.contrib import messages
# Create your views here.
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

    