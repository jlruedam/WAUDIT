from django.urls import path,include
from Auditoria import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('',views.index),
    path('GestionAuditoria/',views.GestionAuditoria, name='GestionAuditoria'),
    path('CrearAuditoria/',views.CrearAuditoria, name='CrearAuditoria'),
    path('EditarAuditoria/',views.EditarAuditoria, name='EditarAuditoria'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)