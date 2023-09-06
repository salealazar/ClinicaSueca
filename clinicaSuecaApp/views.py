from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from clinicaSuecaApp.forms import LoginForm, RegisterForm, BookForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', { 'form': form })

    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('book')
        else:
            return render(request, 'users/register.html', {'form': form})
        
def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('book')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})

def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/login')

def book(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'book.html', { 'form': form })

    if request.method == 'POST':
        
        form = BookForm(request.POST) 
        if form.is_valid():
            book = form.save(commit=False)
            book.paciente = request.user.paciente
            book.save()
            messages.success(request, 'You have booked successfully.')
            return redirect('book')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'book.html', { 'form': form })