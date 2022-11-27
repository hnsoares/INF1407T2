from django.shortcuts import render , redirect , get_object_or_404
from .models import Produto
from datetime import datetime
from .forms import UserForm, ProdutoModel2Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator

from django.urls.base import reverse_lazy
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
        formulario = UserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
        else:
            return render(request,'registro/registro.html',{'form':formulario})
    else:
        # exibe o formulário para criar o usuário
        formulario = UserForm()
        return render(request,'registro/registro.html', {'form': formulario, })

@login_required
def secreto(request):
    return render(request, 'particular/paginaSecreta.html')

class ProdutoListView(View):
    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.all()
        context = { 'produtos': produtos, }
        return render(request,'listaProdutos.html',context)
@method_decorator(login_required, name='dispatch')
class ProdutoListViewSec(View):
    def get(self, request, *args, **kwargs):
        area = request.user.username.split('-')[0]

        #produtos = Produto.objects.all()
        produtos = Produto.objects.filter(setor=area)
        context = { 'produtos': produtos, }
        return render(request,'listaProdutossec.html',context)
        
@method_decorator(login_required, name='dispatch')
class ProdutoUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        #retorna apenas 1 objeto, senão levanta uma excessão
        


        pessoa = Produto.objects.get(pk=pk)
        formulario = ProdutoModel2Form(instance=pessoa)
        setor = formulario.fields['setor']
        setor.widget = setor.hidden_widget()
        context = {'produto': formulario, }
        return render(request, 'atualizaProduto.html', context)

    def post(self, request, pk, *args, **kwargs):
        pessoa = get_object_or_404(Produto, pk=pk)
        formulario = ProdutoModel2Form(request.POST, instance=pessoa)
        if formulario.is_valid():
            pessoa = formulario.save()	
            pessoa.save()									
            return HttpResponseRedirect(reverse_lazy("sec-secreta-read"))
        else:
            contexto = {'produto': formulario, }
            return render(request, 'atualizaProduto.html', contexto)
                
@method_decorator(login_required, name='dispatch')
class ProdutoCreateView(View):
    def get(self, request, *args, **kwargs):
        #retorna apenas 1 objeto, senão levanta uma excessão
        user = request.user.username
        formulario = ProdutoModel2Form()

        setor = formulario.fields['setor']

        setor.initial = user.split('-')[0]
        setor.widget = setor.hidden_widget()
        
        context = {'formulario': formulario}
        return render(request, 'criaProduto.html', context)    

    def post(self, request, *args, **kwargs):
        formulario = ProdutoModel2Form(request.POST)
        user = request.user.username

        if formulario.is_valid():
            produto = formulario.save()   
            produto.save()           
            return HttpResponseRedirect(reverse_lazy('sec-secreta-read')) 
        else:
            return render(request, 'criaProduto.html', {'formulario':formulario})    

@method_decorator(login_required, name='dispatch')
class ProdutoDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        pessoa = Produto.objects.get(pk=pk)
        contexto = { 'produto': pessoa, }
        return render(
            request, 'apagaProduto.html', 
              contexto)

    def post(self, request, pk, *args, **kwargs):
        pessoa = Produto.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect(
            reverse_lazy("sec-secreta-read"))