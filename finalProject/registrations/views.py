# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from registrations.forms import RegisForm, LogForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def registrationsView(request):
    return render(request, 'registration.html', locals())


def registration(request):
    form = RegisForm(request.POST)
    if request.method == "POST" and form.is_valid():

        try:
            form = RegisForm(request.POST)
            form.save()
            return HttpResponseRedirect('/')
        except Exception as e:
            error_str = str(e).split(' ')[9].split('=')[1][1:-1]
            context = {'error':error_str}
            return render(request, 'registration.html', context)


def loginView(request):
    return render(request, 'login.html', locals())

def loging(request):
    form = LogForm(request.POST)

