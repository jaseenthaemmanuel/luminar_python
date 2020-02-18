from django.shortcuts import render, redirect
from books.models import *
from books.forms import *

# Create your views here.
def booklisting(request):
    book= Bookmodel.objects.all()
    dict={}
    dict['object']=book

    return render(request,"books/booklist.html",dict)

def bookcreating(request):
    form = Bookform()

    if request.method =='POST':
        form= Bookform(request.POST)

        if form.is_valid():
            form.save(commit=True)
        return redirect(booklisting)

    return render(request,"books/bookcreate.html",{'form':form})

def bookview(request,pk):
    book = Bookmodel.objects.get(pk=pk)
    context = {'object':book}
    return render(request,"books/bookview.html",context)

def