from django.shortcuts import render
def intro(request):
    return render(request,'introduction/intro.html')
    # def intro(request):
    #     return render(request,'introduction/intro.html')
def hi(request):
    return render(request,"introduction/hi.html")


# Create your views here.
