from django.shortcuts import render,redirect
from tempinher.forms import Loginform
from tempinher.forms import Registerf
from tempinher.models import Employee

def logincontent(request):
    form = Loginform()
    if request == 'GET':
        form = Loginform(request.GET)

    return render(request,'inheritance/Login.html',{'form': form})


def register(request):
    form = Registerf()

    if request.method == 'POST':
        form = Registerf(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("data",form.cleaned_data['name'])
            return redirect(logincontent)
    else:
            return render(request, "inheritance/Register.html", {"form": form})

    return render(request, "inheritance/Register.html", {"form": form})


def tempview(request):
    ob = Employee.objects.all()

    return render(request,"inheritance/View.html",{'ob':ob})