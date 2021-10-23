from django.urls import path,include
from Universo import views


urlpatterns = [
    
    path('UniversoAuditoria/',views.UniversoAuditoria, name='UniversoAuditoria'),
    path('NuevaAuditoriaUniverso/',views.NuevaAuditoriaUniverso, name='NuevaAuditoriaUniverso'),
    path('CargarAuditoriaUniverso/',views.CargarAuditoriaUniverso, name='CargarAuditoriaUniverso'),
    path('GuardarAuditoriaUniverso/',views.GuardarAuditoriaUniverso, name='GuardarAuditoriaUniverso'),
    path('ProcesosAuditarUniverso/',views.ProcesosAuditarUniverso, name='ProcesosAuditarUniverso'),
    path('GuardarGestionResponsable/',views.GuardarGestionResponsable, name='GuardarGestionResponsable'),
    path('GuardarMacroprocesosAuditar/',views.GuardarMacroprocesosAuditar, name='GuardarMacroprocesosAuditar'),
    path('GuardarProcesosAuditar/',views.GuardarProcesosAuditar, name='GuardarProcesosAuditar'),
    path('cargarGestionResponsableUniverso/',views.cargarGestionResponsableUniverso, name='cargarGestionResponsableUniverso'),
    path('aliasHallazgoUniverso/',views.aliasHallazgoUniverso, name='aliasHallazgoUniverso'),
    path('cargarAuditoriaUxCodigo/',views.cargarAuditoriaUxCodigo, name='cargarAuditoriaUxCodigo'),
    
]