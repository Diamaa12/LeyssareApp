from django.contrib import admin

from BleyApp.models import LeyssareMembres, LeyssareCaisse, VersementLeyssare, VersionPeriodique, LeyssareDepenses


# Register your models here.
class LeyssareMembresAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'pays',)
    #cette ligne permet d'effectuer un research sur les prenom, en tapant un caractére et validant par la touche entrée
    search_fields = ("prenom__startswith",)
class CaisseAdmin(admin.ModelAdmin):
    list_display = ('montant_cfa_dispo', 'montant_fg_dispo', 'montant_depencee',)

class VersementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'pays', 'montant_cfa', 'montant_fg',)
    list_filter = ('montant_cfa',)

class PeriodiqueAdmin(admin.ModelAdmin):
    list_display = ('a_versee',)
class DepenseAdmin(admin.ModelAdmin):
    list_display = ('nature_de_depense', 'montant_depensee',)

admin.site.register(LeyssareMembres, LeyssareMembresAdmin)
admin.site.register(VersementLeyssare, VersementAdmin)
admin.site.register(VersionPeriodique, PeriodiqueAdmin)
admin.site.register(LeyssareCaisse, CaisseAdmin)
admin.site.register(LeyssareDepenses, DepenseAdmin)