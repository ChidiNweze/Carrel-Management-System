from django.http import HttpResponse, Http404 
from django.shortcuts import render, redirect
from selection.forms import UserForm, RegistrationForm, LoginForm, SelectForm
from selection.models import Student, Carrel, Floor, Program
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request, *args, **kwargs): 
    # return HttpResponse("<h1>Hello World</h1>") string of html code
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            Student.objects.create(user=new_user)
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login/edit/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = UserForm()
        args = {'form': form}
        return render(request, 'reg_form.html', args)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'profile.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

@login_required
def edit(request):
    if request.method == 'POST':
        data = request.POST.copy()
        form = RegistrationForm(request.POST, instance=request.user.student)
        if form.is_valid():
            form.save()
            return render(request, 'profile.html')
    else:
        form = RegistrationForm(instance=request.user.student)
        return render(request, 'edit.html', {'form': form})  

@login_required
def select(request):
    if request.user.student.Carrel:
        carrel_code_old = request.user.student.Carrel

    if request.method == 'POST':
        form = SelectForm(request.POST, instance=request.user.student)
        if form.is_valid():
            if request.user.student.Carrel:
                request.user.student.carrel_allotted = True
                c_code_after = request.user.student.Carrel
                carrel = Carrel.objects.get(carrel_code=c_code_after)
                carrel.vacant = False
                carrel.save()
                try:
                    carrel = Carrel.objects.get(carrel_code=carrel_code_old)
                    carrel.vacant = True
                    carrel.save()
                except BaseException:
                    pass
            else:
                request.user.student.carrel_allotted = False
                try:
                    carrel = Carrel.objects.get(carrel_code=carrel_code_old)
                    carrel.vacant = True
                    carrel.save()
                except BaseException:
                    pass
            form.save()
            return render(request, 'profile.html')
    else:
        form = SelectForm(instance=request.user.student)
        return render(request, 'select.html', {'form': form})

       
