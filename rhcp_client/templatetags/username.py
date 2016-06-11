# -*- coding: utf-8 -*-
from django import template
from rhcp_client.models import client
register = template.Library()
@register.simple_tag
def client_rus_name(username):
	c = client.objects.get(name=username)
	return c.rus_name
