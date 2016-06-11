# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from rhcp_client.models import client
from rhcp_client.utils import *
# Create your views here.
def index(request):
	return HttpResponse('<h1>RHCP<h1><p><a href="/client">Client area</a></p><p><a href="/testdata">Заполнить тестовыми данными</a></p>')
