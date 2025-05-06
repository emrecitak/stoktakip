from django.db import models

class Sehir(models.Model):
    sehir_adi = models.CharField(max_length=100, unique=True)

    def __str__(self):
      return self.sehir_adi
    
class Ilce(models.Model):
    sehir = models.ForeignKey(Sehir, on_delete=models.CASCADE, related_name='ilceler')
    ilce_adi = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.sehir.sehir_adi} - {self.ilce_adi}"
    
    class Meta:
        unique_together = ('sehir', 'ilce_adi')

class Magaza(models.Model):
    sehir = models.ForeignKey(Sehir, on_delete=models.CASCADE)
    ilce = models.ForeignKey(Ilce, on_delete=models.CASCADE, null=True)
    magaza_adi = models.CharField(max_length=100)
    adres = models.TextField(blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"{self.sehir.sehir_adi} - {self.ilce.ilce_adi if self.ilce else ''} - {self.magaza_adi}"
    
    class Meta:
        unique_together = ('sehir', 'ilce', 'magaza_adi')

class Kategori(models.Model):
    kategori_adi = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.kategori_adi

class Urun(models.Model):
    urun_adi = models.CharField(max_length=100)
    barkod = models.CharField(max_length=50, unique=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, blank=True)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.urun_adi

class Stok(models.Model):
    magaza = models.ForeignKey(Magaza, on_delete=models.CASCADE)
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)
    adet = models.PositiveIntegerField(default=0)
    son_guncelleme = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('magaza', 'urun')
    
    def __str__(self):
        return f"{self.magaza} - {self.urun.urun_adi}: {self.adet} adet"
    
    @property
    def stok_durumu(self):
        if self.adet > 10:
            return "Yeterli Stok"
        elif self.adet > 0:
            return "Sınırlı Stok"
        else:
            return "Stokta Yok"