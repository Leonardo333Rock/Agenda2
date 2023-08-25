from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from . models import Contato


def Agenda(request):
    return render(request,'agenda.html')

@csrf_exempt
def Contato_salvo(request):
    contato = Contato()
    contato.nome = request.POST.get('f_nome')
    contato.celular = request.POST.get('f_celular')
    contato.email = request.POST.get('f_email')
    contato.dtnasc = request.POST.get('f_dtnasc')
    contato.save()

    return redirect('/')
 