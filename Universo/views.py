from django.shortcuts import render
from Universo.models import AuditoriaUniverso, GestionResponsableUniverso, MacroprocesosUniverso, ProcesosUniverso

# Create your views here.

def UniversoAuditoria(request):
    dataAuditoriaU=AuditoriaUniverso.objects.all()
    return render(request,"UniversoAuditoria.html",
                  {
                  "dataAuditoriaU":dataAuditoriaU,
                  }
                  )
    
   

def NuevaAuditoriaUniverso(request):  
    dataGestion=GestionResponsableUniverso.objects.all()
    dataMacro=MacroprocesosUniverso.objects.all()
    dataProceso=ProcesosUniverso.objects.all()  
    return render(request,"NuevaAuditoriaUniverso.html",
                  {
                  "dataGestion":dataGestion,
                  "dataMacro":dataMacro,
                  "dataProceso":dataProceso
                  }
                  )

def CargarAuditoriaUniverso(request):
    
    procesoACargar=request.GET["procesoUniverso2"]
    print(procesoACargar)
    
    dataGestion=GestionResponsableUniverso.objects.all()
    dataMacro=MacroprocesosUniverso.objects.all()
    dataProceso=ProcesosUniverso.objects.all() 
    
    dataProcesoFiltrada=ProcesosUniverso.objects.filter(proceso=procesoACargar)
    print(dataProcesoFiltrada)
    
    
    return render(request,"NuevaAuditoriaUniverso.html",
                  {
                  "dataGestion":dataGestion,
                  "dataMacro":dataMacro,
                  "dataProceso":dataProceso,
                  "dataProcesoFiltrada": dataProcesoFiltrada
                  }
                  )
    
def GuardarAuditoriaUniverso(request):
    
    nuevaAuditU=AuditoriaUniverso(
        proceso=request.GET["procesoUniverso2"],
        macroproceso=request.GET["selectmacroproceso"],
        responsableProceso=request.GET["selectresponsable"],
        codigo=request.GET["CodigoAuditoriaUniverso"],
        auditoriaGeneral=request.GET["AuditoriaGeneralUniverso"],
        nombreAuditoria=request.GET["NombreAuditoriaUniverso"],
        actividadAuditoria=request.GET["ActividadAuditoriaUniverso"],
        riesgosAuditoria=request.GET["RiesgosAuditoriaUniverso"]

    )
    nuevaAuditU.save()
    #También se podría usar el metodo create para crear el objeto en la base de datos
    #Ej: nuevaAuditU=AuditoriaUniverso.Objects.create(aquí los campos a crear)
    dataGestion=GestionResponsableUniverso.objects.all()
    dataMacro=MacroprocesosUniverso.objects.all()
    dataProceso=ProcesosUniverso.objects.all()
    
    
    mensaje="Auditoría Cargada al Universo: CODIGO:%r"%request.GET["CodigoAuditoriaUniverso"]
    
    
    return render(request,"NuevaAuditoriaUniverso.html",
                  {
                  "mensaje":mensaje,
                  "dataGestion":dataGestion,
                  "dataMacro":dataMacro,
                  "dataProceso":dataProceso,               
                  }        
                  )
    

def ProcesosAuditarUniverso(request):
    dataGestion=GestionResponsableUniverso.objects.all()
    dataMacro=MacroprocesosUniverso.objects.all()
    return render(request,"ProcesosAuditarUniverso.html",{'dataGestion':dataGestion,"dataMacro":dataMacro})


def GuardarGestionResponsable(request):
    nuevaGestion=GestionResponsableUniverso(
        responsable=request.GET["gestionResponsableMacro"]   
    )
    nuevaGestion.responsable=nuevaGestion.responsable.replace(" ","_")
    nuevaGestion.save()
    
    dataGestion=GestionResponsableUniverso.objects.all()
    dataMacro=MacroprocesosUniverso.objects.all()
    return render(request,"ProcesosAuditarUniverso.html",{'dataGestion':dataGestion,"dataMacro":dataMacro})


def GuardarMacroprocesosAuditar(request):
    
    nuevoMacroproceso=MacroprocesosUniverso(
        responsable=request.GET["gestionResponsable"],
        macroproceso=request.GET["macroprocesosUniverso"]   
    )
    nuevoMacroproceso.responsable=nuevoMacroproceso.responsable.replace(" ", "_")
    nuevoMacroproceso.macroproceso=nuevoMacroproceso.macroproceso.replace(" ", "_")
    nuevoMacroproceso.save()
    
    dataGestion=GestionResponsableUniverso.objects.all()
    dataMacro=MacroprocesosUniverso.objects.all()
    return render(request,"ProcesosAuditarUniverso.html",{'dataGestion':dataGestion,"dataMacro":dataMacro})

 
def GuardarProcesosAuditar(request): 
    
    nuevoProceso=ProcesosUniverso(
        proceso=request.GET["procesosUniversoCargar"],
        macroproceso=request.GET["macroprocesosUniverso"],
        responsable=request.GET["gestionElegida"],
    )
    nuevoProceso.proceso=nuevoProceso.proceso.replace(" ","_")
    nuevoProceso.save()

        
    dataGestion=GestionResponsableUniverso.objects.all()
    dataMacro=MacroprocesosUniverso.objects.all()
    mensajeProceso="Proceso cargado a la base datos: "+nuevoProceso.proceso
    
    
    return render(request,"ProcesosAuditarUniverso.html",{'dataGestion':dataGestion,"dataMacro":dataMacro, "mensajeProceso":mensajeProceso})
   

def cargarGestionResponsableUniverso(request): 
    
    gestionResponsable=request.GET["gestionResponsable"]
    macroProcesosCargar=MacroprocesosUniverso.objects.filter(responsable=gestionResponsable)
    print(macroProcesosCargar)
    
    dataGestion=GestionResponsableUniverso.objects.all()
    dataMacro=MacroprocesosUniverso.objects.all()
    return render(request,"ProcesosAuditarUniverso.html",{'dataGestion':dataGestion,"dataMacro":dataMacro,"gResponsable":gestionResponsable,"macroProcesosCargar": macroProcesosCargar})
    
    
def aliasHallazgoUniverso(request):
    dataAuditoriaUniverso=AuditoriaUniverso.objects.all()
    
    return render(request,"aliasHallazgoUniverso.html",{'dataAuditoriaUniverso':dataAuditoriaUniverso})

def cargarAuditoriaUxCodigo(request):
    codigoCargar = request.GET["selectCodigo"]
    dataAuditoriaUFiltrada=AuditoriaUniverso.objects.filter(codigo=codigoCargar)
    
    dataAuditoriaUniverso=AuditoriaUniverso.objects.all()
    dF=(dataAuditoriaUFiltrada.values())[0]
    print(dF)
    return render(request,"aliasHallazgoUniverso.html",{'dataAuditoriaUniverso':dataAuditoriaUniverso,"dataAuditoriaUFiltrada":dF})
    