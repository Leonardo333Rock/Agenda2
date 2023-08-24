from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from . models import Contato


def Agenda(request):
    return render(request,'agenda.html')

@csrf_exempt
def Contato_salvo(request):
    contato = Contato()
    nome = request.POST.get('f_nome')
    celular = request.POST.get('f_celular')
    email = request.POST.get('f_email')
    dtnasc = request.POST.get('f_dtnasc')

    return redirect('/')
