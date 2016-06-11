# -*- coding: utf-8 -*-
import sys
from suds.client import Client
from suds import WebFault
from suds.sax.element import Element
from suds.xsd.doctor import Import
from suds.xsd.doctor import ImportDoctor
from suds.plugin import MessagePlugin

class UnicodeFilter(MessagePlugin):
    def received(self, context):
        decoded = context.reply.decode('utf-8', errors='ignore')
        reencoded = decoded.encode('utf-8')
        context.reply = reencoded

class Filter(MessagePlugin):
    def received(self, context):
        reply = context.reply
        context.reply = reply[reply.find("<s:Envelope"):reply.rfind(">")+1]

url = 'https://partner.r01.ru:1443/partner_api.khtml?wsdl'
#tns = 'urn:RegbaseSoapInterface'
def pr_pr(st):
    sys.stdout.flush()
    sys.stdout.write(st)

print 'Коннектимся к R01'
client = Client(url)#, retxml=False, faults=False)
pr_pr('\rOk')
##imp = Import('http://schemas.xmlsoap.org/soap/encoding/', 'http://schemas.xmlsoap.org/soap/encoding/')
##imp.filter.add(tns)
##client = Client(url, retxml = True, plugins=[ImportDoctor(imp), Filter(), UnicodeFilter()])
##print client
##loginResult = client.logIn('UD/04/9362', 'YSA05051977')
loginResult = client.service.logIn('testreseller', 'testreseller')
if loginResult.status.code == '0':
	print 'Не удалось подключиться'
	exit()

print loginResult.status.code
print loginResult.status.name
print loginResult.status.message
print

print 'Устанавливаем SOAPClient'
client = Client(url, headers={'Cookie':'SOAPClient=%s'%loginResult.status.message})
print 'Ok'

result = client.service.getAbonents()
print result.status.code
print result.status.name
print result.status.message
print
for ab in result.data:
	print ab.parent_agr_number + ' ' + ab.agr_number

pr_pr('Отключаемся - ')
client.service.logOut()
pr_pr('Ok')
print
print 'Готово'

