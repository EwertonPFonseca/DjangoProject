from django.contrib import admin
from .models import *

class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome','data_criacao','data_modificao']
    search_fields = ['nome']
# Register your models here.
admin.site.register(Pessoa, PessoaAdmin)