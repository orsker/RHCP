# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-09 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rhcp_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0441\u0438\u0441\u0442\u0435\u043c\u044b')),
                ('email', models.EmailField(max_length=50, verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430')),
                ('password', models.CharField(max_length=50, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c')),
                ('nic_hdl', models.CharField(max_length=50, null=True, verbose_name='Nic-hdl \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430')),
                ('client_type', models.CharField(choices=[['MAN', '\u0424\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043b\u0438\u0446\u043e'], ['IND', '\u0418\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u0435\u043b\u044c'], ['ORG', '\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f']], default='MAN', max_length=3, verbose_name='\u0422\u0438\u043f \u043a\u043b\u0438\u0435\u043d\u0442\u0430')),
                ('date_add', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'rhcp_client',
                'verbose_name': '\u041a\u043b\u0438\u0435\u043d\u0442',
                'verbose_name_plural': '\u041a\u043b\u0438\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='client_domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100, verbose_name='\u0414\u043e\u043c\u0435\u043d')),
                ('date_reg', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhcp_client.client')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhcp_core.domain_tariff')),
            ],
            options={
                'db_table': 'rhcp_client_domain',
                'verbose_name': '\u0414\u043e\u043c\u0435\u043d \u043a\u043b\u0438\u0435\u043d\u0442\u0430',
                'verbose_name_plural': '\u0414\u043e\u043c\u0435\u043d\u044b \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='client_site_tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhcp_client.client')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhcp_core.site_tariff')),
            ],
            options={
                'db_table': 'rhcp_client_site_tariff',
                'verbose_name': '\u0422\u0430\u0440\u0438\u0444 \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u043d\u0430 \u0441\u0430\u0439\u0442',
                'verbose_name_plural': '\u0422\u0430\u0440\u0438\u0444\u044b \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432 \u043d\u0430 \u0441\u0430\u0439\u0442',
            },
        ),
        migrations.CreateModel(
            name='ind_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='\u0418\u043c\u044f')),
                ('second_name', models.CharField(max_length=50, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('third_name', models.CharField(max_length=50, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhcp_client.client')),
            ],
            options={
                'ordering': ['third_name'],
                'db_table': 'rhcp_ind_info',
                'verbose_name': '\u0414\u0430\u043d\u043d\u044b\u0435 \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u0435\u043b\u044f',
                'verbose_name_plural': '\u0414\u0430\u043d\u043d\u044b\u0435 \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u044b\u0445 \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u0435\u043b\u0435\u0439',
            },
        ),
        migrations.CreateModel(
            name='man_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='\u0418\u043c\u044f')),
                ('second_name', models.CharField(max_length=50, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('third_name', models.CharField(max_length=50, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('eng_name', models.CharField(default='', max_length=150, verbose_name='\u0424\u0418\u041e \u043f\u043e \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438')),
                ('passport', models.CharField(default='', max_length=150, verbose_name='\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430')),
                ('date_born', models.DateField(blank=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430')),
                ('post_address', models.CharField(default='', max_length=250, verbose_name='\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441')),
                ('phones', models.CharField(default='', max_length=100, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u044b')),
                ('faxes', models.CharField(default='', max_length=100, verbose_name='\u0424\u0430\u043a\u0441\u044b')),
                ('emails', models.CharField(default='', max_length=100, verbose_name='\u0415\u043c\u0430\u0439\u043b\u044b')),
                ('resident', models.BooleanField(default=True, verbose_name='\u0420\u0435\u0437\u0438\u0434\u0435\u043d\u0442 \u0420\u0424')),
                ('inn', models.CharField(default='', max_length=12, verbose_name='\u0418\u041d\u041d')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhcp_client.client')),
            ],
            options={
                'ordering': ['third_name'],
                'db_table': 'rhcp_man_info',
                'verbose_name': '\u0414\u0430\u043d\u043d\u044b\u0435 \u0444\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043b\u0438\u0446\u0430',
                'verbose_name_plural': '\u0414\u0430\u043d\u043d\u044b\u0435 \u0444\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043b\u0438\u0446',
            },
        ),
        migrations.CreateModel(
            name='org_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhcp_client.client')),
            ],
            options={
                'ordering': ['caption'],
                'db_table': 'rhcp_org_info',
                'verbose_name': '\u0414\u0430\u043d\u043d\u044b\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438',
                'verbose_name_plural': '\u0414\u0430\u043d\u043d\u044b\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0439',
            },
        ),
    ]