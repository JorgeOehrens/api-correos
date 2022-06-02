from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Correo
# Register your models here.
@admin.register(Correo)
class CorreoAdmin(ImportExportModelAdmin):
    list_display = ('empresa','correo_cliente','correo_admin','asunto','mensaje','creado')
