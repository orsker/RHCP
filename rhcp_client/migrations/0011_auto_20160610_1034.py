# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-10 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rhcp_client', '0010_client_date_last'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='r01_nic_hdl',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nic-hdl \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430 \u0434\u043e\u043c\u0435\u043d\u043e\u0432'),
        ),
        migrations.AlterField(
            model_name='client',
            name='r01_password',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c R01 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430 \u0434\u043e\u043c\u0435\u043d\u043e\u0432'),
        ),
        migrations.AlterField(
            model_name='client',
            name='r01_username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f R01 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430 \u0434\u043e\u043c\u0435\u043d\u043e\u0432'),
        ),
    ]