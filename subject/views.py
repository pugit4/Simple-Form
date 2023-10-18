from django.shortcuts import render, redirect
from .models import Mytopic
from .forms import mytopicform

# Create your views here.
def create_view(request):
    if request.method == "POST":
       form = mytopicform(request.POST) 
       if form.is_valid():
           form.save()
           return redirect('lv')
    else:
        form = mytopicform()
    return render(request, 'create.html',{'form':form})
       
       
def list_view(request):
    items = Mytopic.objects.all()
    return render(request, 'list.html', {'items':items})


def update_view(request, id):
    item = Mytopic.objects.get(id=id)
    if request.method == "POST":
        form = mytopicform(request.POST, instance=item)
        if form.is_valid():
           form.save()
           return redirect('lv')
    else:
        form = mytopicform(instance=item)
    return render(request, 'update.html', {'form': form})


def delete_view(request, id):
    item = Mytopic.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect('lv')
    return render(request, 'delete.html', {'item': item})
        
    
       
          