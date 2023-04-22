from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .data import Company
import time
from datetime import datetime

@login_required(login_url='signin')
def home(request):
	number = request.POST.get('number')

	company = Company(number)
	context = {"infos":company.company_data()}

	return render(request, "home.html", context)


def Company_data(request):
	number = request.POST.get('number')

	company = Company(number)
	context = {"infos":company.company_data()}

	return render(request, "department.html", context)


def Department_data(request):
	number = request.POST.get('number')

	company = Company(number)
	context = {"infos":company.company_data()}

	return render(request, "home.html", context)


def Personal_data(request):
	number = request.POST.get('number')

	company = Company(number)
	context = {"infos":company.company_data()}

	return render(request, "personal.html", context)


def Delete_data(request):
	number = request.POST.get('number')

	company = Company(number)
	context = {"infos":company.company_data()}

	return render(request, "delete.html", context)




