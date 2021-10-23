from django.db import models

# Create your models here.
class AuditoriaUniverso(models.Model):
    proceso=models.CharField(max_length=100)
    macroproceso=models.CharField(max_length=100)
    responsableProceso=models.CharField(max_length=50)
    codigo=models.CharField(max_length=8)
    auditoriaGeneral=models.CharField(max_length=50)
    nombreAuditoria=models.CharField(max_length=50)
    actividadAuditoria=models.CharField(max_length=150)
    riesgosAuditoria=models.CharField(max_length=150,null=True)
    
    
"""  
class MacroprocesosUniverso(models.Model):
    macroproceso=models.CharField(max_length=100)
    
"""  
class GestionResponsableUniverso(models.Model):
    responsable=models.CharField(max_length=100)
    
class MacroprocesosUniverso(models.Model):
    macroproceso=models.CharField(max_length=100)
    responsable=models.CharField(max_length=100)
    
class ProcesosUniverso(models.Model):
    responsable=models.CharField(max_length=100,null=True)
    macroproceso=models.CharField(max_length=100)
    proceso=models.CharField(max_length=100)
    
class aliasUniverso(models.Model):
    alias=models.CharField(max_length=100,null=True)
    codigo=models.CharField(max_length=100)
    
    
    
    
    
    
    
    
    