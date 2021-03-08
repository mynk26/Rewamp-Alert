from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm,SignupForm
from django.views import View
from django.contrib.auth import login, authenticate, logout
# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'LoginForm.html', {'form':form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../Dashboard/')
            else:
                return HttpResponse("<script>window.location.href = './'; alert('Incorrect UserName/Password');</script>")
        else:
            return render(request, 'LoginForm.html', {'form': form, 'field.errors': form.errors})

class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'SignupForm.html', {'form':form})
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('../Dashboard/')
        else:
            return render(request, 'SignupForm.html', {'form': form, 'field.errors': form.errors})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse("<script>window.location.href = '../';alert('Logged out successfully!');</script>")