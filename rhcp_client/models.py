# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from rhcp_core.models import site
# Create your models here.

class client(models.Model):
	CL_MAN = 'MAN'
	CL_IND = 'IND'
	CL_ORG = 'ORG'
	TYPE_OF_CLIENT = [
		[CL_MAN, 'Физическое лицо'],
		[CL_IND, 'Индивидуальный предприниматель'],
		[CL_ORG, 'Организация'],
	]
	name = models.CharField('Пользователь системы RHCP', max_length=50, null=False, blank=False)
	email = models.EmailField('Электронная почта пользователя системы RHCP', max_length=50, null=False,blank=False)
	password = models.CharField('Пароль порльзователя системы RHCP', max_length=50, null=False, blank=False)
	r01_nic_hdl = models.CharField('Nic-hdl администратора доменов', max_length=50, null=True, blank=True)
	r01_username = models.CharField('Имя пользователя R01 администратора доменов', max_length=50, null=True, blank=True)
	r01_password = models.CharField('Пароль R01 администратора доменов', max_length=50, null=True, blank=True)
	client_type = models.CharField('Тип клиента', max_length=3, choices=TYPE_OF_CLIENT, default=CL_MAN, null=False, blank=False)
	date_add = models.DateField('Дата регистрации пользователя системы RHCP', auto_now_add=True, null=False, blank=False)
	date_last = models.DateField('Дата последнего входа в систему RHCP', null=True, blank=True)
	# INFO
	
	rus_name = models.CharField('ФИО или наименование по-русски', max_length=150, null=True)
	eng_name = models.CharField('ФИО или наименование по-английски', max_length=150, null=True)
	passport = models.CharField('Паспортные данные администратора', max_length=150, null=True)
	date_born = models.DateField('Дата рождения администратора', null=True)
	post_address = models.CharField('Почтовый адрес', max_length=250, null=True)
	phones = models.TextField('Телефоны', max_length=500, null=True)
	faxes = models.TextField('Факсы', max_length=500, null=True)
	emails = models.TextField('Емайлы', max_length=500, null=True)
	resident = models.BooleanField('Резидент РФ', default=True)
	inn = models.CharField('ИНН', max_length=12, null=True, blank=True)
	kpp = models.CharField('КПП', max_length=12, null=True, blank=True)
	ogrn = models.CharField('ОГРН', max_length=12, null=True, blank=True)
	jur_address = models.CharField('Юридический адрес', max_length=250, null=True, blank=True)
	chief_name = models.CharField('ФИО руководителя организации', max_length=150, null=True, blank=True)
	bank = models.CharField('Название банка', max_length=150, null=True, blank=True)
	rs = models.CharField('Расчётный счёт', max_length=20, null=True, blank=True)
	ks = models.CharField('Корреспондентский счёт', max_length=20, null=True, blank=True)
	bik = models.CharField('БИК', max_length=150, null=True, blank=True)
	class Meta:
		db_table = 'rhcp_client'
		ordering = ['name']
		verbose_name = 'Клиент'
		verbose_name_plural = 'Клиенты'
	def __unicode__(self):
		return self.name




#class client_domain_tariff(models.Model):
#	client = models.ForeignKey(client, on_delete=models.CASCADE)
#	tariff = models.ForeignKey(domain_tariff)
#	class Meta:
#		db_table = 'rhcp_client_domain_tariff'
#		verbose_name = 'Тариф клиента на домен'
#		verbose_name_plural = 'Тарифы клиентов на домен'
#	def __unicode__(self):
#		return self.client + ':' + self.tariff

#class client_domain(models.Model):
#	client = models.ForeignKey(client, on_delete=models.CASCADE)
#	tariff = models.ForeignKey(domain_tariff)
#	domain = models.CharField('Домен', max_length=100, null=False, blank=False)
#	date_reg = models.DateField('Дата создания', null=False, blank=False)
#	class Meta:
#		db_table = 'rhcp_client_domain'
#		verbose_name = 'Домен клиента'
#		verbose_name_plural = 'Домены клиентов'
#	def __unicode__(self):
#		return self.domain

