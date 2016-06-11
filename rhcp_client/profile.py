# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.signing import Signer
from django.conf import settings
import os
import sys
from django import forms
import logging, logging.config
from utils import *
from models import client
from django.utils.dateparse import parse_date


# -----------------------------------------------------
# Профиль клиента
#

def c_login(request):
	if request.method == 'POST':
		try:
			s = client.objects.get(Q(email=request.POST['useremail']) & Q(password=signedpasswd(request.POST['userpass'])))
		except (KeyError, client.DoesNotExist):
			return render(request, 'c_login.html', {
				'formmessage': 'Email или пароль указны неверно',
			})
		else:
			request.session['username'] = s.name
			return redirect('client')
	else:
		return render(request, 'c_login.html')


def c_restorepasswd(request):
	if request.method == 'POST':
		try:
			s = client.objects.get(email=request.POST['useremail'])
		except (KeyError, client.DoesNotExist):
			return render(request, 'c_restorepasswd.html', {
				'formmessage': 'Клиента с таким email не существует',
				'formmessage_class': 'alert alert-danger',
			})
		else:
			newpasswd = str(User.objects.make_random_password())
			s.password = signedpasswd(newpasswd)
			s.save()
			body = '<HTML><BODY>'
			body += 'Вы запросили восстановление пароля.<br>'
			body += 'Сейчас система установила для Вас пароль: <strong>'
			body += newpasswd
			body += '</strong>.<br>'
			body += 'Войдите в систему с этим паролем и поменяйте его.<br>'
			body += '</BODY></HTML>'
			send_mail('Восстановление пароля', '', 'orsk-cariolis@surw.rzd', ['orsk-cariolis@surw.rzd'], fail_silently=False, html_message=body)
			return render(request, 'c_restorepasswd.html', {
				'formmessage': 'На указанный email выслана инструкция по смене пароля',
				'formmessage_class': 'alert alert-success',
			})
	else:
		return render(request, 'c_restorepasswd.html')


def c_changepasswd(request):
	if not c_security(request): return redirect('c_login')
	if request.method == 'POST':
		s = client.objects.get(name=request.session['username'])
		s.password = signedpasswd(request.POST['userpassword'])
		s.save()
		request.session['message'] = 'Пароль изменён.'
		return redirect('c_profile')
	else:
		return render(request, 'c_changepasswd.html')


def c_logout(request):
	request.session.clear()
	request.session.flush()
	return redirect('c_login')


def c_reg(request):
	if request.method == 'POST':
		uname = request.POST['username']
		uemail = request.POST['useremail']
		upass = request.POST['userpassword']
		utype = request.POST['usertype']
		try:
			s = client.objects.get(name=request.POST['username'])
		except (KeyError, client.DoesNotExist):
			try:
				s = client.objects.get(email=request.POST['useremail'])
			except (KeyError, client.DoesNotExist):
				s = client()
				s.name = uname
				s.password = signedpasswd(upass)
				s.email = uemail
				s.client_type = utype
				s.nic_hdl = None
				s.save()
				request.session.clear()
				request.session['username'] = uname
				return redirect('client')
			else:
				message = 'Клиент с таким email уже существует'
				return render(request, 'c_reg.html', {
					'formmessage': message,
					'uname': uname
				})
		else:
			message = 'Клиент с таким именем уже существует'
			return render(request, 'c_reg.html', {
					'formmessage': message,
					'uemail': uemail
				})
	else:
		return render(request, 'c_reg.html')


def c_profile(request):
	if not c_security(request): return redirect('c_login')
	return render(request, 'c_profile.html', {
		'username': request.session['username'],
		'message': SiteMessage(request),
		'message_type': SiteMessageType(request)
	})

def c_info(request):
	if not c_security(request): return redirect('c_login')
	c = client.objects.get(id= getid(request))
	if request.method == 'POST':
		c.rus_name = request.POST['rus_name'].strip()
		c.eng_name = request.POST['eng_name'].strip()
		if request.POST.get('passport'): c.passport = request.POST.get('passport').strip()
		if request.POST.get('date_born'): c.date_born = parse_date(request.POST.get('date_born'))
		c.post_address = request.POST['post_address'].strip()
		c.phones = request.POST['phones'].strip()
		c.faxes = request.POST['faxes'].strip()
		c.emails = request.POST['emails'].strip()
		if request.POST.get('resident') == 'on':
			c.resident = True
		else:
			c.resident = False
		c.inn = request.POST['inn'].strip()
		if request.POST.get('kpp'): c.kpp = request.POST.get('kpp').strip()
		if request.POST.get('ogrn'): c.ogrn = request.POST.get('ogrn').strip()
		if request.POST.get('jur_address'): c.jur_address = request.POST.get('jur_address').strip()
		if request.POST.get('chief_name'): c.chief_name = request.POST.get('chief_name').strip()
		if request.POST.get('bank'): c.bank = request.POST.get('bank').strip()
		if request.POST.get('rs'): c.rs = request.POST.get('rs').strip()
		if request.POST.get('ks'): c.ks = request.POST.get('ks').strip()
		if request.POST.get('bik'): c.bik = request.POST.get('bik').strip()
		c.save()
		request.session['message'] = 'Данные сохранены'
		request.session['message_type'] = 'success'
		return redirect('c_profile')
	else:
		if 'message' not in request.session:
			request.session['message'] = 'Внимание! Контроль корректности вводимых данных не проводится, будьте внимательны.'
			request.session['messag_type'] = 'info'
		return render(request, 'c_info.html', {
			'username': request.session['username'],
			'c':c,
			'message': SiteMessage(request),
			'message_type': SiteMessageType(request)
		})
