# -*- coding: utf-8 -*-
from django.shortcuts import redirect
import logging, logging.config
import sys
from django.core.signing import Signer
from django.conf import settings
from models import client

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}
logging.config.dictConfig(LOGGING)
#logging.info('Starting client utils...')



# -----------------------------------------------------
# Утилиты
#

def c_security(request):
	if 'username' not in request.session:
		return False
	else:
		return True

#def s_sendmail(request):
#	send_mail('Тема', 'вапрвапр', settings.EMAIL_FROM_ADDR, ['orsk-cariolis@surw.rzd'], fail_silently=False)
#	return HttpResponse('письмо отправлено')

#def s_adminsendmail(body):
#	send_mail('Сообщение от системы молла', '', settings.EMAIL_FROM_ADDR, [settings.ADMIN_EMAIL], fail_silently=False, html_message=body)

def signedpasswd(password):
	signer = Signer(salt=settings.SALT)
	return signer.sign(password).split(':')[1]

def getid(request):
	obj = client.objects.get(name = request.session['username'])
	return obj.id

def getclient(request):
	return client.objects.get(id=getid(request))


def SiteMessage(request):
	if 'message' not in request.session:
		return None
	else:
		mess = request.session['message']
		del request.session['message']
		return mess

def SiteMessageType(request):
	if 'message_type' not in request.session:
		return None
	else:
		mess = request.session['message_type']
		del request.session['message_type']
		return mess


def UserErrors(request):
	c = client.objects.get(id = getid(request))
	if c.rus_name == None: return [True, 'c_info']
	elif c.rus_name.strip() == '': return [True, 'c_info']
	elif c.eng_name == None: return [True, 'c_info']
	elif c.eng_name.strip() == '': return [True, 'c_info']
	elif c.passport == None: return [True, 'c_info']
	elif c.passport.strip() == '': return [True, 'c_info']
	elif c.date_born == None: return [True, 'c_info']
	#elif date_born == None: return [True, 'c_info']
	elif c.post_address == None: return [True, 'c_info']
	elif c.post_address.strip() == '': return [True, 'c_info']
	elif c.phones == None: return [True, 'c_info']
	elif c.phones.strip() == '': return [True, 'c_info']
	elif c.faxes == None: return [True, 'c_info']
	elif c.faxes.strip() == '': return [True, 'c_info']
	elif c.emails == None: return [True, 'c_info']
	elif c.emails.strip() == '': return [True, 'c_info']
	elif c.resident == None: return [True, 'c_info']
	#elif c.resident.strip() == '': return [True, 'c_info']
	elif c.inn == None: return [True, 'c_info']
	elif c.inn.strip() == '': return [True, 'c_info']
	
	if c.client_type == 'ORG':
		if c.kpp == None: return [True, 'c_info']
		elif c.kpp.strip() == '': return [True, 'c_info']
		elif c.ogrn == None: return [True, 'c_info']
		elif c.ogrn.strip() == '': return [True, 'c_info']
		elif c.jur_address == None: return [True, 'c_info']
		elif c.jur_address.strip() == '': return [True, 'c_info']
		elif c.chief_name == None: return [True, 'c_info']
		elif c.chief_name.strip() == '': return [True, 'c_info']
		elif c.bank == None: return [True, 'c_info']
		elif c.bank.strip() == '': return [True, 'c_info']
		elif c.rs == None: return [True, 'c_info']
		elif c.rs.strip() == '': return [True, 'c_info']
		elif c.ks == None: return [True, 'c_info']
		elif c.ks.strip() == '': return [True, 'c_info']
		elif c.bik == None: return [True, 'c_info']
		elif c.bik.strip() == '': return [True, 'c_info']
		
	return[False, '']

