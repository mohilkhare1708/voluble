from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from mainapp.models import WordForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
    return render(request, 'mainapp/home.html', {'title' : 'Home'})

@login_required
def choice_page(request):
    return render(request, 'mainapp/choice.html', {'title' : 'Choose'})

@login_required
def revise_page(request):
    return render(request, 'mainapp/revise.html', {'title' : 'Revise'})

@login_required
def add_word_page(request):
    form = WordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            word = form.cleaned_data.get('word')
            user = request.user
            user.profile.words.append(word)
            user.save()
            return redirect('choice-page')
    return render(request, 'mainapp/addWord.html', {'title' : 'Add Word', 'form' : form})

def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.full_name = form.cleaned_data.get('full_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.phone = form.cleaned_data.get('phone')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('login-page')
    else:
        print("bro")
        form = UserRegisterForm()
    return render(request, 'mainapp/register.html', {'title' : 'Register', 'form' : form})

@login_required
def addWord_page(request):
    return render(request, 'mainapp/revise.html', {'title' : 'Revise'})