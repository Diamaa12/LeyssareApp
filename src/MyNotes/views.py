from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import SamedNotes, MamadouNotes

# Create your views here.

def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method == 'POST':
        print(username, password)
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                #Cette fonction permet de connecter la personne à la page d'admin de Django.
                login(request, user)
                data = MamadouNotes.objects.all().order_by('-id').values()
                data2 = SamedNotes.objects.all().order_by('-id').values()
                username = username.lower()
                if username == 'mamadou':
                    return render(request, f"{username}.html", {'data': data})
                elif username == 'samed':
                    return render(request, f"{username}.html", {'data': data2})
            else:
                messages.success(request, ('Username or Password falls. '))
                print('Your are not connected.')
                return redirect('Mynotes:login-user')
        else:
            messages.error(request, ('The Username is falls. '))
            return redirect('Mynotes:login-user')
    else:

        return render(request, "connection.html")
    return render(request, "registration/login.html")

def user_logout(request):
        if request.user.is_authenticated == True:
            username = request.user.username
        else:
            username = None

        return username
def logout_view(request):
    username = user_logout(request)
    if username != None:
        print(f'{username} you are loged out. ')
        logout(request)
        return render(request, 'connection.html', {'ticks':'Please enter your Username end Password to reconnect. '})

@login_required(login_url='../../Mynotes/login/')
def mamadou_notes(request):
    if request.method == 'POST':
        jours = request.POST.get('day')
        post = request.POST.get('notes')
        date = request.POST.get('date')
        usr = MamadouNotes(day=jours, notes=post, date=date)
        usr.save()
        notes = MamadouNotes.objects.all().order_by('-id').values()
        return render(request, 'mamadou.html', {'data':notes})
    elif request.method == 'GET':
        notes = MamadouNotes.objects.all().order_by('-id').values()
        return render(request, 'mamadou.html', {'data':notes})
    return render(request, 'mamadou.html', {'error':'No data to print. '})
@login_required(login_url='../../Mynotes/login')
def mamadou_items_del(request, id):
    items = MamadouNotes.objects.get(id=id)
    user = user_logout(request)
    items.delete()

    usr = user.lower()
    context = {'del':'You have delete this items', 'user':usr}
    return render(request, 'items_del.html', context)
@login_required(login_url="../../Mynotes/login/")
def samed_notes(request):
    if request.method == 'POST':
        jours = request.POST.get('day')
        post = request.POST.get('notes')
        date = request.POST.get('date')
        usr = SamedNotes(day=jours, notes=post, date=date)
        usr.save()
        notes = SamedNotes.objects.all().order_by('-id').values()
        return render(request, 'samed.html', {'data':notes})
    elif request.method == 'GET':
        notes = MamadouNotes.objects.all().order_by('-id').values()
        return render(request, 'mamadou.html', {'data':notes})
    return render(request, 'samed.html', {'error':'No data to print. '})
@login_required(login_url='../../Mynotes/login/')
def samed_items_del(request, id):
    items = SamedNotes.objects.get(id=id)
    user = user_logout(request)
    items.delete()

    usr = user.lower()
    context = {'del':'You have delete this items', 'user':usr}

    return render(request, 'items_del.html', context)
