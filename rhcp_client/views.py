# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from utils import *
#from models import client, man_info, org_info, ind_info

# Create your views here.
def client(request):
	if c_security(request):
		u_e = UserErrors(request)
		if u_e[0]:
			#print '### UserErrors is'
			request.session['message'] = 'Для работы в системе обязательно заполните свои данные'
			request.session['message_type'] = 'error'
			return redirect(u_e[1])
		else:
			return render (request, 'c_dashboard.html', {
				'username': request.session['username'],
			})
	else:
		return redirect('c_login')
