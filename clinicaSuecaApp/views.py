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
    pass

def sign_out(request):
    pass

def book(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'book.html', { 'form': form })

    if request.method == 'POST':
        
        form = BookForm(request.POST, paciente=request.user.paciente) 
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            messages.success(request, 'You have booked successfully.')
            return redirect('book')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'book.html', { 'form': form })