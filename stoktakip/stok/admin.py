from django.contrib import admin
from .models import Sehir, Ilce, Magaza, Kategori, Urun, Stok

class IlceInline(admin.TabularInline):
    model = Ilce
    extra = 1

class SehirAdmin(admin.ModelAdmin):
    inlines = [IlceInline]
    list_display = ('sehir_adi',)
    search_fields = ('sehir_adi',)

class MagazaAdmin(admin.ModelAdmin):
    list_display = ('magaza_adi', 'sehir', 'ilce', 'telefon')
    list_filter = ('sehir', 'ilce')
    search_fields = ('magaza_adi', 'adres')

class UrunAdmin(admin.ModelAdmin):
    list_display = ('urun_adi', 'barkod', 'kategori', 'fiyat')
    list_filter = ('kategori',)
    search_fields = ('urun_adi', 'barkod')

class StokAdmin(admin.ModelAdmin):
    list_display = ('magaza', 'urun', 'adet', 'stok_durumu', 'son_guncelleme')
    list_filter = ('magaza__sehir', 'magaza__ilce', 'magaza')
    search_fields = ('urun__urun_adi', 'urun__barkod')

admin.site.register(Sehir, SehirAdmin)
admin.site.register(Ilce)
admin.site.register(Magaza, MagazaAdmin)
admin.site.register(Kategori)
admin.site.register(Urun, UrunAdmin)
admin.site.register(Stok, StokAdmin)
