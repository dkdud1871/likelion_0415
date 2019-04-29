from django.shortcuts import render,get_object_or_404,redirect
from .models import Person
from .forms import PersonForm
# Create your views here.
def home(request):
    
    persons=Person.objects
    return render(request,'portfolio/home.html', {'persons':persons})
def detail(request,person_id):
   person_detail =get_object_or_404(Person,pk=person_id)
   
   return render(request, 'portfolio/detail.html',{'person':person_detail})    
def new(request):
    if request.method=='POST':
        form=PersonForm(request.POST)
        if form.is_valid():
            person=form.save(commit=False)
            person.save()
            #return redirect('detail',Person_id=person.id)
            return redirect('home')

    else:
        form=PersonForm()
        return render(request, 'portfolio/new.html',{'form':form})    

   
def edit(request,person_id):
    post=get_object_or_404(Person, pk=person_id)
    if request.method=='POST':
        form=PersonForm(request.POST,instance=post)
        if form.is_valid():
            person=form.save(commit=False)
            person.save()
            #return redirect('detail',Person_id=person.id)
            return redirect('home')

    else:
        form=PersonForm(instance=post)
        return render(request, 'portfolio/edit.html',{'form':form}) 

def delete(request,person_id):
    person=get_object_or_404(Person,pk=person_id) 
    person.delete()
    return redirect('home')       
