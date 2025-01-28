from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.template import loader
from django.http import HttpResponse


def get_context(title, d=None):
    context = {'title': title,
               'pages': [('football/', 'Футбол'),
                         ]}
    if d:
        for k in d:
            context[k] = d[k]
    return context


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('/')
    else:

        form = UserRegisterForm()
        template = loader.get_template("users/register.html")
        context = get_context('Главная страница', {'form': form})
        return HttpResponse(template.render(context,request))
# Create your views here.
