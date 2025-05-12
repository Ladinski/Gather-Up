from django.contrib.auth import  login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

User = get_user_model()
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    login_failed = False
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            login_failed = True
    return render(request, 'accounts/login.html', {'form': form, 'login_failed': login_failed})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')  
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            error = "Username already exists"
            return render(request, 'accounts/signup.html', {'error': error})
        
        user = User.objects.create_user(username=username, email=email, password=password) 
        login(request, user)
        return redirect('home')
    
    return render(request, 'accounts/signup.html')


@login_required(login_url='/accounts/login/')
def profile_view(request):
    return render(request, 'accounts/profile.html')

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')

