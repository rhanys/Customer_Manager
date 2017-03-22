from django.shortcuts import render, redirect
from core.models import Customer
from django.http import HttpResponseRedirect
from core.forms import CustomerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

username = 'null'

# Create your views here.
"""
def login(request):
    customer_list = Customer.objects.all
    form = CustomerForm()
    context_alter = {'customers': customer_list}
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            c = Customer()
            c.name = form.cleaned_data["name"]
            c.save()
            return redirect("/dashboard/")
        else:
            form = CustomerForm()
    context_dict = {'customers': customer_list, 'form': form}
    return render(request, 'index.html', context_dict)"""

def logar(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                username = request.POST['username']
                return redirect("/dashboard/")
            else:
                return render(request, 'index.html', {"form": form})
        return render(request, 'index.html', {"form": AuthenticationForm()})

   

def dashboard(request):
    return render(request, 'dashboard.html')
