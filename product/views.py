from django.shortcuts import render, redirect
from django.http import Http404
from product.forms import signupForm, loginForm
from product.models import User, Product
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = make_password(form.cleaned_data.get('password'))
            phone = form.cleaned_data.get('phone')
            username = form.cleaned_data.get('username')
            User.objects.create(name=name, email=email, password=password, phone=phone, username=username)
            return redirect('login')
        else:
            raise Http404
    else:
        form = signupForm()
    return render(request, 'signup.html', {'form' : form})

def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            u = User.objects.filter(username=username).values(password)
            if check_password(password, u[0]['password']):
                request.session['logged_in'] = True
            else:
                return redirect('login')
            return redirect('list')
        else:
            raise Http404
    else:
        form = loginForm()
    return render(request, 'login.html', {"form" : form})

def logout(request):
    del request.session['logged_in']
    return redirect('login')

def list(request):
    if request.session['logged_in'] == True:
        data = Product.objects.all().values()
        return render(request, 'list.html',  {"data": data})
    else:
        return redirect('login')

def detail(request, pk):
    if request.session['logged_in'] == True:
        data = Product.objects.filter(pk=pk)
        return render(request, 'detail.html', {"data": data})
    else:
        return redirect('login')