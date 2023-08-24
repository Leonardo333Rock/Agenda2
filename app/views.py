from django.shortcuts import render


def Agenda(request):
    return render(request,'agenda.html')