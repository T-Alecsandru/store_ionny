from django.contrib import admin
from ionny.models import *


class ProduseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'promoted')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')


admin.site.register(Produse, ProduseAdmin)
admin.site.register(Contact, ContactAdmin)
