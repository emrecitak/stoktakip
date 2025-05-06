from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.urun_arama, name='urun_arama'),
    path('get_ilceler/', views.get_ilceler, name='get_ilceler'),
    path('get_magazalar/', views.get_magazalar, name='get_magazalar'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)