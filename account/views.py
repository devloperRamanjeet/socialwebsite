from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated'
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('invalid login')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    h= int(now.hour)

    if  h <= 12:
        s='Good Morning'
    elif h < 16:
        s=f'Good Afternoon'
    else:
        s=f'Good Night'
    return render(request,
                  'account/dashboard.html',
                  {'section': dashboard,
                   'time':s })
