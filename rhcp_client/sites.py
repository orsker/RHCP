# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from utils import *

# Create your views here.
def c_sites(request):
	if c_security(request):
		return render (request, 'c_sites.html', {
			'username': request.session['username'],
			'sites': getSites()
		})
	else:
		return redirect('c_login')


# -----------------------
# действия
#
def getSites():
	result = ['wer', 'asd', 'zxc']
	return result
