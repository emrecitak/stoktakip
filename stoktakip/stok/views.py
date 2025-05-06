from django.shortcuts import render
from django.http import JsonResponse
from .models import Sehir, Ilce, Magaza, Urun, Stok

def urun_arama(request):
    query = request.GET.get('q', '')
    sehir_id = request.GET.get('sehir', '')
    ilce_id = request.GET.get('ilce', '')
    magaza_id = request.GET.get('magaza', '')
    stok_durumu = request.GET.get('stok_durumu', '')
    
   
    sehir_secildi = 'sehir' in request.GET and request.GET['sehir'] != None
    
   
    if sehir_secildi:
        stoklar = Stok.objects.select_related('magaza', 'urun', 'magaza__sehir', 'magaza__ilce')
        
        
        if query:
            stoklar = stoklar.filter(urun__urun_adi__icontains=query) | stoklar.filter(urun__barkod__icontains=query)
        
     
        if sehir_id and sehir_id != '':
            stoklar = stoklar.filter(magaza__sehir_id=sehir_id)
        
        if ilce_id:
            stoklar = stoklar.filter(magaza__ilce_id=ilce_id)
        
        if magaza_id:
            stoklar = stoklar.filter(magaza_id=magaza_id)
        
        if stok_durumu:
            if stok_durumu == 'var':
                stoklar = stoklar.filter(adet__gt=0)
            elif stok_durumu == 'az':
                stoklar = stoklar.filter(adet__gt=0, adet__lte=10)
            elif stok_durumu == 'yok':
                stoklar = stoklar.filter(adet=0)
    else:
       
        stoklar = []
    
    
    sehirler = Sehir.objects.all()
    
    return render(request, 'stoktakip/urun_arama.html', {
        'stoklar': stoklar, 
        'query': query,
        'sehirler': sehirler,
        'secili_sehir_id': sehir_id,
        'secili_ilce_id': ilce_id,
        'secili_magaza_id': magaza_id,
        'secili_stok_durumu': stok_durumu,
        'sehir_secildi': sehir_secildi
    })

def get_ilceler(request):
    sehir_id = request.GET.get('sehir_id')
    ilceler = []
    
    if sehir_id:
        ilceler = list(Ilce.objects.filter(sehir_id=sehir_id).values('id', 'ilce_adi'))
    
    return JsonResponse(ilceler, safe=False)

def get_magazalar(request):
    sehir_id = request.GET.get('sehir_id')
    ilce_id = request.GET.get('ilce_id')
    magazalar = []
    
    if ilce_id:
        magazalar = list(Magaza.objects.filter(ilce_id=ilce_id).values('id', 'magaza_adi'))
    elif sehir_id:
        magazalar = list(Magaza.objects.filter(sehir_id=sehir_id).values('id', 'magaza_adi'))
    
    return JsonResponse(magazalar, safe=False)