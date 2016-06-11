from django.contrib import admin
from models import site_tariff, domain_tariff, site
# Register your models here.
admin.site.register(site_tariff)
admin.site.register(domain_tariff)
admin.site.register(site)
