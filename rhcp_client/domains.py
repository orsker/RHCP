# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from suds.client import Client
from suds import WebFault
from utils import *

# Create your views here.
def c_domains(request):
	if not c_security(request): return redirect('c_login')
	#if client.objects.get(id=getid(request)).r01_nic_hdl == None:
	#	return redirect('c_r01reg')
	return render (request, 'c_domains.html', {
		'username': request.session['username'],
		#'domains': getDomains()
	})

def c_r01_reg(request):
	if not c_security(request): return redirect('c_login')
	#res = getAbonents()
	res = regAdmin(getclient(request))
	if res[0]:
		return HttpResponse('Готово! nic-hdl: ' + res[1])
	else:
		return HttpResponse('Ошибка: ' + res[1])


# -----------------------
# действия
#

def regAdmin(c):
	try:
		client = Client(settings.R01_URL)
		conn = client.service.logIn(settings.R01_USER, settings.R01_PASSWORD)
		client = Client(settings.R01_URL, headers={'Cookie':'SOAPClient=%s'%conn.status.message})
		if c.client_type == 'MAN':
			result = client.service.addDadminPerson('OL100-GPT', c.rus_name, c.eng_name, c.passport, '01-01-1980', c.post_address, c.phones, c.faxes, c.emails, 1, 1, c.inn)
			print result
	except WebFault, e:
		return [False, e]
	else:
		if result.status.code == 1:
			return [True, result.status.message]
		else:
			return [False, result.status.message.encode('utf-8')]

def getAbonents():
	try:
		client = Client(settings.R01_URL)
		conn = client.service.logIn(settings.R01_USER, settings.R01_PASSWORD)
		client = Client(settings.R01_URL, headers={'Cookie':'SOAPClient=%s'%conn.status.message})
		result = client.service.getAbonents()
		#for ab in result.data:
		#	print ab.parent_agr_number + ' ' + ab.agr_number
	except WebFault, e:
		return [False, e]
	else:
		return [True, result.data]
