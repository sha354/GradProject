from django.shortcuts import render, redirect
from .models import *
from . import forms
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'core/home.html')


def clubs_list(request):
    clubs = User.objects.all()
    data= {'clubs': clubs}
    return render(request, 'core/clubs_list.html', data)


def club_details(request, slug):  # include club_courses
    club = Profile.objects.get(slug=slug)
    data= {'club': club}
    return render(request, 'core/club_details.html', data)


def sign_up(request):
    if request.method == 'POST':
       form = forms.UserCreationForms(request.POST)  # Store it in form-variable to check
       if form.is_valid():  # its fields are complete and correct.
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # like the name of field in UserCreationForms
            user = authenticate(username=username, password=password)
            login(request, user)  # Do login
            return redirect('core:home')
    else:
        form = forms.UserCreationForms()  # return empty form
    data={'form': form}
    return render(request, 'core/sign_up.html', data)


def login_info(request):
    if request.method == 'POST':
        form = forms.LoginForm()
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username=username, password=password)  # checking user-data is Signed-up before or not
        if user is not None:
            login(request, user)  # Do login
            return redirect('core:home')
    else:
        form = forms.LoginForm()
    data={'form': form}
    return render(request, 'core/login.html', data)


def my_profile(request):
    return render(request,'core/my_profile.html')


def update_profile(request):
    user_form = forms.UpdateUserForm(instance=request.user)
    profile_form = forms.UpdateProfileForm(instance=request.user.profile)
    # when you apply any change:
    if request.method == 'POST':
        user_form = forms.UpdateUserForm(request.POST, instance=request.user)  # form= UpdateUserForm= form req+ first,last name of curr user
        profile_form = forms.UpdateProfileForm( request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect('core:home')

    data = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'core/update_profile.html', data)
