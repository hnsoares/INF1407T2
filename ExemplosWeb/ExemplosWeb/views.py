from django.shortcuts import render , redirect
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def homepage(request):
    agora = datetime.now()
    relogio = {
    "dia" :agora.day,
    "mes" :agora.month ,
    "ano" :agora.year ,
    "hora" :agora.hour ,
    "minuto" :agora.minute ,
    }   

    return render(request,'ExemplosWeb/index.html',relogio)

def homeSec(request):
    return render(request,"registro/homeSec.html")


    
def registro(request):
    if request.method =='POST':
        #cria um novo usuário no banco de dados
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
        else:
            return render(request,'registro/registro.html',{'form':formulario})
    else:
        # exibe o formulário para criar o usuário
        formulario = UserCreationForm()
        return render(request,'registro/registro.html', {'form': formulario, })

@login_required
def secreto(request):
    return render(request, 'particular/paginaSecreta.html')