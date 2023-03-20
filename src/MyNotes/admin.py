
from django.contrib import admin
from MyNotes.models import SamedNotes, MamadouNotes

from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(SamedNotes)
#admin.site.register(MamadouNotes)



class MamadouNotesAdmin(ImportExportModelAdmin):
        list_display = ('day', 'notes',)


admin.site.register(MamadouNotes, MamadouNotesAdmin)
