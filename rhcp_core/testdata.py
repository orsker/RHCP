# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from rhcp_client.models import client
from rhcp_core.models import domain_tariff, site_tariff
from rhcp_client.utils import *
from pytils.translit import translify
# Create your views here.

def testdata(request):
	# клиенты
	# физик
	c = client()
	c.name = 'man'
	c.email = 'man@rhcp.ru'
	c.password = signedpasswd('12345')
	c.client_type = 'MAN'
	c.r01_nic_hdl = None
	c.r01_username = None
	c.r01_password = None
	#c.save()
	
	#cinfo = man_info()
	#cinfo.client_id = c.id
	c.rus_name = 'Ман Манович Манов'
	c.eng_name = translify(c.rus_name.decode('utf-8'))
	c.passport = '12 03 №321456 выдан ОВД Кировского района г. Ленинграда 24.02.1980'
	c.date_born = '1970-01-12'
	c.post_address = '450001, г. Ленинград, ул. Луговая, д. 44, кв. 12'
	c.phones = '79014568432'
	c.faxes = '79014568432'
	c.emails = 'man@rhcp.ru'
	c.resident = True
	c.inn = '345123678543'
	c.save()
	
	# ип
	c = client()
	c.name = 'ind'
	c.email = 'ind@rhcp.ru'
	c.password = signedpasswd('12345')
	c.client_type = 'IND'
	c.r01_nic_hdl = None
	c.r01_username = None
	c.r01_password = None
	#c.save()
	
	#cinfo = ind_info()
	#cinfo.client_id = c.id
	c.rus_name = 'Инд Индович Индов'
	c.eng_name = translify(c.rus_name.decode('utf-8'))
	c.passport = '12 03 №321456 выдан ОВД Кировского района г. Ленинграда 24.02.1980'
	c.date_born = '1970-01-12'
	c.post_address = '450001, г. Ленинград, ул. Луговая, д. 44, кв. 12'
	c.phones = '79014568432'
	c.faxes = '79014568432'
	c.emails = 'man@rhcp.ru'
	c.resident = True
	c.inn = '345123678543'
	c.save()
	
	# контора
	c = client()
	c.name = 'org'
	c.email = 'org@rhcp.ru'
	c.password = signedpasswd('12345')
	c.client_type = 'ORG'
	c.r01_nic_hdl = None
	c.r01_username = None
	c.r01_password = None
	#c.save()
	
	#cinfo = org_info()
	#cinfo.client_id = c.id
	c.rus_name = 'ООО "Рога и копыта"'
	c.eng_name = translify(c.rus_name.decode('utf-8'))
	c.post_address = '450001, г. Ленинград, ул. Луговая, д. 44, кв. 12'
	c.phones = '79014568432'
	c.faxes = '79014568432'
	c.emails = 'man@rhcp.ru'
	c.resident = True
	c.inn = '345123678543'
	c.kpp = '123456789012'
	c.ogrn = '123456789012'
	c.jur_address = '450001, г. Ленинград, ул. Луговая, д. 44, кв. 12'
	c.chief_name = 'Пётр Петрович Петров'
	c.bank = 'Банк Развитие'
	c.rs = '11111222223333344444'
	c.ks = '55555666667777788888'
	c.bik = '123456789'
	c.save()
	
	# тарифы доменов
	#dt = domain_tariff()
	#dt.name = 'простой ru'
	
	#dt.zone = 'ru'
	#dt.price = 600
	
	#dt.active = True
	#dt.date_inactive = None
	#dt.save()
	
	# тарифы сайтов
	#st = site_tariff()
	#st.name = 'простой'
	
	#st.space = 500
	#st.support = False
	#st.price = 600
	#st.year_discount = 10
	
	#st.active = True
	#st.date_inactive = None
	#st.save()
	return redirect('index')
