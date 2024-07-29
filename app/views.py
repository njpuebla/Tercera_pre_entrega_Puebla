from django.shortcuts import render
from app.forms import ElectricaFormulario
from app.forms import AcusticaFormulario
from app.forms import AmplificadoreFormulario
from app.forms import EfectoFormulario

# Create your views here.
def inicio(request):
    return render(request, 'app/index.html')

def electrica(request):
    if request.method == "POST":
        el_formulario = ElectricaFormulario(request.POST) 
        if el_formulario.is_valid():
            informacion = el_formulario.cleaned_data
            
            electrica = electrica (marca=informacion["marca"], modelo=informacion["modelo"])
            electrica.save()

            return render(request, "app/index.html")
    else:
        el_formulario = ElectricaFormulario()

    return render(request, 'app/electricas.html', {"el_formulario": el_formulario})

def acusticas(request):
    if request.method == "POST":
        ac_formulario = AcusticaFormulario(request.POST) 
        if ac_formulario.is_valid():
            informacion = ac_formulario.cleaned_data
            
            acusticas = acusticas (marca=informacion["marca"], modelo=informacion["modelo"])
            acusticas.save()

            return render(request, "app/index.html")
    else:
        ac_formulario = AcusticaFormulario()

    return render(request, 'app/acusticas.html', {"ac_formulario": ac_formulario})

def amplificadores(request):
    if request.method == "POST":
        am_formulario = AmplificadoreFormulario(request.POST) 
        if am_formulario.is_valid():
            informacion = am_formulario.cleaned_data
            
            amplificadores = amplificadores (marca=informacion["marca"], modelo=informacion["modelo"])
            acusticas.save()

            return render(request, "app/index.html")
    else:
        am_formulario = AmplificadoreFormulario()

    return render(request, 'app/amplificadores.html', {"am_formulario": am_formulario})    

def efectos(request):
    if request.method == "POST":
        ef_formulario = EfectoFormulario(request.POST) 
        if ef_formulario.is_valid():
            informacion = ef_formulario.cleaned_data
            
            efectos = efectos (marca=informacion["marca"], modelo=informacion["modelo"])
            acusticas.save()

            return render(request, "app/index.html")
    else:
        ef_formulario = EfectoFormulario()

    return render(request, 'app/efectos.html', {"ef_formulario": ef_formulario}) 