from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def connexion(request):
    return render(request,"connexion.html")

def inscription(request):
    return render(request,"inscription.html")

def outil(request):
    return render(request,'outil.html')

def index_log(request):
    return render(request,'index_log.html')

def messagerie(request):
    return render(request,'messagerie.html')

def outil_log(request):
    return render(request,'outil_log.html')

def profile(request):
    return render(request,'profile.html')