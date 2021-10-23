from django.urls import path,include
from Auditoria import views


urlpatterns = [
    
    path('',views.index),
    path('GestionAuditoria/',views.GestionAuditoria, name='GestionAuditoria'),
    path('CrearAuditoria/',views.CrearAuditoria, name='CrearAuditoria'),
    path('EditarAuditoria/',views.EditarAuditoria, name='EditarAuditoria'),
]