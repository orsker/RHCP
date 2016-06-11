# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rhcp_client.models import client

# Create your models here.
class site_tariff(models.Model):
	name = models.CharField('Имя', max_length=50, null=False, blank=False)
	
	space = models.IntegerField('Дисковое пространство', null=False, blank=False)
	support = models.BooleanField('Техподдержка', null=False, blank=False)
	price = models.IntegerField('Цена за месяц', null=False, blank=False)
	year_discount = models.IntegerField('Скидка при оплате за год, %', null=False, blank=False)
	
	active = models.BooleanField('Действующий', null=False, blank=False)
	date_add = models.DateField('Дата создания', auto_now_add=True, null=False, blank=False)
	date_stop = models.DateField('Дата отключения', null=True)
	class Meta:
		db_table = 'rhcp_site_tariff'
		ordering = ['name']
		verbose_name = 'Тариф сайта'
		verbose_name_plural = 'Тарифы сайтов'
	def __unicode__(self):
		return self.name
		
class site(models.Model):
	site_tariff = models.ForeignKey(site_tariff)
	client = models.ForeignKey(client, on_delete=models.CASCADE)
	name = models.CharField('Имя', max_length=150, null=False, blank=False)
	#active = models.BooleanField('Действующий', null=False, blank=False, default=False)
	date_add = models.DateField('Дата создания', auto_now_add=True, null=False, blank=False)
	date_stop = models.DateField('Дата приостановки', null=True)
	class Meta:
		db_table = 'rhcp_site'
		ordering = ['name']
		verbose_name = 'Сайт'
		verbose_name_plural = 'Сайты'
	def __unicode__(self):
		return self.name


class domain_tariff(models.Model):
	name = models.CharField('Имя', max_length=50, null=False, blank=False)
	
	zone = models.CharField('Зона 1 первого уровня', max_length=20, null=False, blank=False)
	price = models.IntegerField('Цена за домен в год', null=False, blank=False)
	
	active = models.BooleanField('Действующий', null=False, blank=False)
	date_add = models.DateField('Дата создания', auto_now_add=True, null=False, blank=False)
	date_stop = models.DateField('Дата отключения', null=True)
	class Meta:
		db_table = 'rhcp_domain_tariff'
		ordering = ['name']
		verbose_name = 'Тариф домена'
		verbose_name_plural = 'Тарифы доменов'
	def __unicode__(self):
		return self.name
	

