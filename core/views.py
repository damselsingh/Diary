from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm, SignUpForm, DiaryForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Diary
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in successfully.')
                    return HttpResponseRedirect('/dashboard/')
                else:
                    return HttpResponseRedirect('/')
        else:
            form= LoginForm
            return render(request, 'core/home.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/dashboard/')          
    else :
        form = SignUpForm()
    return render(request, 'core/user_signup.html', {'form': form})

def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        data = Diary.objects.filter(user=user).order_by('-id')[:5]
        if request.method == 'POST':
            defineday = request.POST['defineday']
            write = request.POST['write']
            new = Diary(defineday=defineday, write=write, user=request.user)
            new.save()
            messages.success(request, 'succesfully saved!')
            return HttpResponseRedirect('/dashboard/')
        else: 
            form = DiaryForm()
            count=Diary.objects.all().count()
        return render(request, 'core/dashboard.html', {'form': form, 'data': data, 'count': count})
    else:
        messages.success(request, 'login required!')
        return HttpResponseRedirect('/')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You are logged out')
        return HttpResponseRedirect('/')
    else:
        messages.success(request, 'login required!')
        return HttpResponseRedirect('/')

def show_journal(request, pk):
    if request.user.is_authenticated:
        form = Diary.objects.get(id=pk)
        return render(request, 'core/journal.html', {'form': form})
    else:
        messages.success(request, 'login required!')
        return HttpResponseRedirect('/')

def journal_delete(request, pk):
    if request.user.is_authenticated:
        deldata = Diary.objects.get(id=pk)
        deldata.delete()
        messages.success(request, 'You successfully deleted a page!')
        return HttpResponseRedirect('/dashboard/')
    else:
        messages.success(request, 'login required!')
        return HttpResponseRedirect('/')

def journal_update(request, pk):
    if request.user.is_authenticated:
        updata = Diary.objects.get(id=pk)
        forms = DiaryForm(instance=updata)
        if request.method == 'POST':
            forms = DiaryForm(request.POST, instance=updata)
            if forms.is_valid():
                forms.save()
                messages.success(request, 'updated!')
                return HttpResponseRedirect('/dashboard/')
        return render(request, 'core/update.html', {'forms': forms})
    else:
        messages.success(request, 'login required!')
        return HttpResponseRedirect('/')

def extra(request):
    if request.user.is_authenticated:
        user = request.user
        data = Diary.objects.filter(user=user)
        return render(request, 'core/extra.html', {'data': data})
    else:
        messages.success(request, 'login required!')
        return HttpResponseRedirect('/')