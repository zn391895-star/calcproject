from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse
import math

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
        else:
            messages.error(request, "Invalid input. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login')
def calculator(request):
    return render(request, 'calculator.html')

from django.shortcuts import render

def home(request):
    return render(request, "calculator.html")


@login_required
def calculator(request):
    return render(request, 'calculator.html')




@login_required(login_url='login')
def calculate_expression(request):
    if request.method == "POST":
        expr = request.POST.get("expression", "")
        try:
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            result = eval(expr, {"__builtins__": {}}, allowed_names)
        except Exception:
            result = "Error"
        return JsonResponse({"result": result})
    

def logout_view(request):
    logout(request)
    return redirect('login')



