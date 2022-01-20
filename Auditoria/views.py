from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,"templates/index.html")
    
def GestionAuditoria(request):
    return render(request,"GestionAuditoria.html")

def CrearAuditoria(request):
    return render(request,"crearAuditoria.html")

def EditarAuditoria(request):
    cod=["Auditoria-"+str(x+1) for x in range(10)]
    return render(request,"editarAuditoria.html",{"codigo":cod})


