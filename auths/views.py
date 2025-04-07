from django.shortcuts import render, redirect
from auths.forms import RegisterForm
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from auths.models import Register
from django.contrib.auth.decorators import login_required

def Register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        form_data = {
            'username': username,
            'email': email,
            'password': password
        }
        
        form = RegisterForm(form_data)
        if form.is_valid():
            
            register = form.save()
            
            
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                auth_login(request, user)
                messages.success(request, 'Kayıt başarılı! Hoş geldiniz.')
                return redirect("home")
            except Exception as e:
                messages.error(request, f'Kullanıcı oluşturma hatası: {str(e)}')
        else:
            messages.error(request, 'Formda hata var. Lütfen tekrar deneyin.')
    
    return render(request, 'register.html')
@login_required
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Geçersiz kullanıcı adı veya şifre')
            
    return render(request, 'login.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('dashboard')
    else:
        return redirect('dashboard')